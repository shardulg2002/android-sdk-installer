# android-sdk-installer

![License](https://img.shields.io/badge/License-GNU%20v3.0-blue?style=for-the-badge)  ![Python](https://img.shields.io/badge/Language-Python-3670A0?style=for-the-badge&logo=python&logoColor=white)

### CLI tool for Android SDK installation and environment setup

---

## Disclaimer

This project is intended **for personal use only**.
Use at your own risk; the author is not responsible for any damage or issues caused by running this software.

---

## Usage

### Option 1: Run without installation
1. **Clone the repository:**
```bash
git clone https://github.com/andrey4ik21pro1/android-sdk-installer.git
cd android-sdk-installer
```
2. **Install dependencies:**
```bash
pip install -r requirements.txt
```
3. **Run**:
- Linux/macOS: `./run.sh --path sdk`
- Windows: `.\run.ps1 --path sdk` or `.\run.bat --path sdk`

### Option 2: Install as a system command (Recommended)
1. **Install the package:**
```bash
pip install .
```
2. **Run**:
- `android-sdk-installer --path sdk`

---

## License

This project is distributed under the **GNU General Public License
v3.0**.\
See the `LICENSE` file for details.
