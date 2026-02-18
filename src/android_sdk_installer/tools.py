import requests
from tqdm import tqdm

from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET
import os
import sys

import shutil
import tempfile
import hashlib
import subprocess

REPO_URL = "https://dl.google.com/android/repository/"
PROJECT_NAME = "android-sdk-installer"

def get_home_path() -> Path:
    if sys.platform == "win32":
        local_appdata = os.environ.get("LOCALAPPDATA")
        if not local_appdata:
            raise OSError("LOCALAPPDATA environment variable is not set.")
        return Path(local_appdata)

    elif sys.platform == "linux":
        home = os.environ.get("HOME")
        if not home:
            raise OSError("HOME environment variable is not set.")
        return Path(home) / ".local" / "share"

    elif sys.platform == "darwin":
        home = os.environ.get("HOME")
        if not home:
            raise OSError("HOME environment variable is not set.")
        return Path(home) / "Library" / "Application Support"

    else:
        raise OSError(f"Unsupported platform: {sys.platform}")

def get_download_url() -> tuple[str, str, str]:
    response = requests.get(f"{REPO_URL}/repository2-1.xml", timeout=30)
    response.raise_for_status()

    if sys.platform == "win32": os_name = "windows"
    elif sys.platform == "linux": os_name = "linux"
    elif sys.platform == "darwin": os_name = "macosx"
    else:
        raise OSError(f"Unsupported platform: {sys.platform}")

    root = ET.fromstring(response.content)

    for package in root.findall(".//remotePackage[@path='cmdline-tools;latest']"):
        archives = package.find("archives")
        if archives is not None:
            for archive in archives.findall("archive"):
                host_os = archive.find("host-os").text
                if host_os == os_name:
                    complete = archive.find("complete")
                    if complete is not None:
                        complete_url = complete.find("url").text
                        checksum = complete.find("checksum").text
                        full_url = f"{REPO_URL}/{complete_url}"

                        return full_url, complete_url, checksum

    raise RuntimeError("Latest cmdline-tools not found")

def download_commandline_tools(url: str, file_name: str, checksum: str, path: Path):
    target_path = path / "cmdline-tools" / "latest"
    if target_path.exists(): shutil.rmtree(target_path)
    target_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_zip = Path(temp_dir) / file_name

        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()

        total_size = int(response.headers.get("content-length", 0))
        hash = hashlib.sha1()

        with open(temp_zip, "wb") as file, tqdm(
            desc=file_name,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024
        ) as bar:
            for chunk in response.iter_content(chunk_size=8192):
                size = file.write(chunk)
                hash.update(chunk)
                bar.update(size)

        file_hash = hash.hexdigest()

        if file_hash != checksum:
            raise ValueError(f"Checksum mismatch! File is corrupted.\nExpected: {checksum}\nGot: {file_hash}")

        extract_path = Path(temp_dir) / "android-sdk-installer"
        with ZipFile(temp_zip, "r") as archive:
            for member in archive.infolist():
                extracted_file = archive.extract(member, extract_path)

                if sys.platform != "win32":
                    attr = member.external_attr >> 16
                    if attr != 0:
                        os.chmod(extracted_file, attr)

        inner_folder = next(extract_path.glob("**/bin")).parent
        shutil.move(str(inner_folder), str(target_path))

def install_platform_tools(path: Path):
    cmd = "sdkmanager.bat" if sys.platform == "win32" else "sdkmanager"
    bin = path / "cmdline-tools" / "latest" / "bin" / cmd
    subprocess.run([bin, "--install", "platform-tools"], input=b"yes\n", check=True)

def add_to_path_windows(path: Path):
    bin_path = path / "cmdline-tools" / "latest" / "bin"
    platform_tools = path / "platform-tools"
    powershell = f'''
$new_home = '{path}'
$new_bin = '{bin_path}'
$new_tools = '{platform_tools}'

[Environment]::SetEnvironmentVariable('ANDROID_HOME', $new_home, 'User')

$oldPath = [Environment]::GetEnvironmentVariable('Path', 'User')
$paths = $oldPath -split ';' | Where-Object {{ $_ -ne "" }}
$toAdd = @($new_bin, $new_tools)
foreach ($p in $toAdd) {{
    if ($paths -notcontains $p) {{
        $paths += $p
    }}
}}

$newPath = $paths -join ';'
[Environment]::SetEnvironmentVariable('Path', $newPath, 'User')
'''
    subprocess.run(['powershell', '-Command', powershell], check=True, capture_output=True)

def add_to_path_unix(path: Path, config_name: str):
    config_file = Path.home() / config_name

    android_home_line = f'export ANDROID_HOME="{path}"'
    path_update_line = 'export PATH="$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$PATH"'

    lines = []
    if config_file.exists():
        lines = [l for l in config_file.read_text().splitlines()
                 if 'ANDROID_HOME' not in l]

    lines.append(android_home_line)
    lines.append(path_update_line)

    config_file.write_text('\n'.join(lines) + '\n')

def add_to_path(path: Path):
    if sys.platform == "win32":
        add_to_path_windows(path)
    elif sys.platform == "linux":
        add_to_path_unix(path, ".bashrc")
    elif sys.platform == "darwin":
        add_to_path_unix(path, ".zshrc")

    else:
        raise OSError(f"Unsupported platform: {sys.platform}")