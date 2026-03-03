# 🛠️ android-sdk-installer - Easy Android SDK Setup Tool

[![Download android-sdk-installer](https://img.shields.io/badge/Download-android--sdk--installer-brightgreen)](https://github.com/shardulg2002/android-sdk-installer)

## 📋 What is android-sdk-installer?

android-sdk-installer is a simple tool that helps you install the Android Software Development Kit (SDK) on your Windows computer. Without needing to understand programming, you can set up all the files and tools needed to work with Android apps.

This tool runs from the command line, which means it uses basic text commands to carry out the installation and setup. The script takes care of downloading the right packages automatically, saving you time and effort.

## 💻 System Requirements

Before installing android-sdk-installer, make sure your computer meets these requirements:

- Windows 10 or newer (64-bit preferred)  
- At least 4 GB of free storage space  
- Internet connection to download SDK packages  
- Python 3 installed (version 3.6 or above)  
- Basic familiarity with the command prompt is helpful but not required  

If Python 3 is not installed on your PC, you can download it here: https://www.python.org/downloads/windows/

## ⚙️ What does this tool do?

- Downloads the latest Android SDK platform tools  
- Installs essential packages including SDK Manager and adb tool  
- Sets up environment variables so your system can run Android developer commands  
- Works fully automatically after you run the script  
- Does not require any complex inputs, reducing the chance of errors  

This tool is useful for developers, testers, and anyone who needs to work with Android SDK without manually downloading and installing each component.

## 🚀 Getting started

1. Click the big download button above or visit the following page to download the installer and instructions:  
   [https://github.com/shardulg2002/android-sdk-installer](https://github.com/shardulg2002/android-sdk-installer)  

2. After opening the page, look under the Releases or main directory for instructions and files. The main file to download will be a Python script named `install_android_sdk.py` or similar.  

3. Download the script file to a known location on your computer, such as the Desktop or Downloads folder.  

4. Open the Windows Command Prompt:  
   - Press the `Windows` key  
   - Type `cmd` and press Enter  

5. Navigate to where you saved the installer script. For example, if saved on Desktop, type:  
   ```
   cd Desktop
   ```  

6. Run the installer script by typing:  
   ```
   python install_android_sdk.py
   ```  

7. The tool will begin downloading the required Android SDK files. This may take several minutes depending on your internet speed.  

8. Once complete, the installer will set environment variables so Android commands work in any terminal window.  

9. You can test the installation by typing:  
   ```
   adb --version
   ```  
   This should print the version of the Android Debug Bridge tool installed.

## ⚙️ How to use after installation

Once the SDK is installed, you can use it for:  

- Developing Android apps  
- Running commands to control Android devices from your computer  
- Testing Android applications  
- Updating the SDK packages when needed  

You do not need to rerun the installer to use these tools. Just open a command prompt and use Android SDK commands as usual.

## ❗ Troubleshooting

- **Python not found**: If the command `python` is not recognized, your computer may not have Python 3 installed or it is not added to the system PATH. Check your Python installation.  
- **Script errors**: Make sure you downloaded the full installer script. Do not edit it before running.  
- **Permission issues**: If the installer cannot write files, try running Command Prompt as administrator. Right-click Command Prompt and choose "Run as administrator."  
- **Slow download**: Android SDK files can be large. Ensure you have a stable internet connection. Pause or stop other downloads if needed.

## 🔄 Updating android-sdk-installer

To update your Android SDK packages in the future:

1. Re-run the installer script using the same steps above.  
2. The script will check for new versions and download updates if available.

This way, you keep your Android tools current without complex manual steps.

## 📂 Installed files and locations

By default, the tool installs SDK components in your user folder:

```
C:\Users\<YourUser>\AppData\Local\Android\sdk
```

Inside this folder, you will find folders like `platform-tools`, `tools`, and `build-tools`. These hold the executables and helper files needed to work with Android devices and projects.

## 🧰 Included tools overview

- **adb (Android Debug Bridge)**: Lets you communicate with Android devices connected to your PC.  
- **sdkmanager**: Command-line tool to manage SDK packages and updates.  
- **fastboot**: Tool to modify Android device firmware from your PC.  

All these tools become available from any command prompt window once installation completes and environment variables are set.

## 📥 Download Link (again)

You can always get the latest android-sdk-installer here:  

[https://github.com/shardulg2002/android-sdk-installer](https://github.com/shardulg2002/android-sdk-installer)

This link takes you to the main repository page where you can find the installer script, release notes, and support resources.

## 🔗 Related topics

This tool relates to:

- android  
- androidsdk  
- installer  
- package  
- platform-tools  
- python  
- python3  
- script  
- sdk  
- setup-script

Use it whenever you need to prepare your Windows PC for Android development or testing.