# Anti-Forensics Toolkit (User Manual)

Anti-Forensics Toolkit aims to securely delete selected files, securely delete known forensic artifacts, and manipulate timestamps of selected files.

## Table Of Contents

- [Anti-Forensics Toolkit (User Manual)](#anti-forensics-toolkit-user-manual)
  * [Table Of Contents](#table-of-contents)
  * [Getting Started](#getting-started)
    + [Requirements](#requirements)
    + [Libraries](#libraries)
    + [Executing the program](#executing-the-program)
      1. [Option One (Secure Delete)](#option-one-secure-delete)
      2. [Option Two (Delete file opening artifacts)](#option-two-delete-file-opening-artifacts)
      3. [Option Three (Delete USB Registry Key Identification)](#option-three-delete-usb-registry-key-identification)
      4. [Option Four (Delete Browser Artifacts)](#option-four-delete-browser-artifacts)
      5. [Option Five (Change timestamps)](#option-five-change-timestamps)
      6. [Option Six (Exit)](#option-six-exit)
  * [Authors](#authors)


## Getting Started

### Requirements

- Windows 10
- Python 3 (if running the .py file instead of .exe)


### Libraries

- win32-setfiletime
```
pip install -r requirements.txt
```

### Executing the program

- Run the script or the pre-compiled binary to bring up a menu of choices.
```
python3 anti-forensics-toolkit.py
```

```
.\anti-forensics-toolkit.exe
```
![Menu](images/menu.png)


#### Option One (Secure Delete)

1. Enter "1" as the choice.
2. Specify one or more files to securely delete, with each file separated by a "|".
3. Proceed with the deletion when prompted.

![Secure Delete](images/secure-delete.png)

#### Option Two (Delete file opening artifacts)

1. Enter "2" as the choice.
2. Proceed with the deletion when prompted.

![Delete File-opening Artifacts](images/delete-file-opening-artifacts.png)

#### Option Three (Delete USB Registry Key Identification)

1. Enter "3" as the choice.
2. Proceed with the deletion when prompted.

![Delete USB Registry Key Identification](images/delete-usb-key-info.png)


#### Option Four (Delete Browser Artifacts)

1. Enter "4" as the choice.
2. Proceed with the deletion when prompted.

![Delete Browser Artifacts](images/delete-browser-artifacts.png)


#### Option Five (Change timestamps)

1. Enter "5" as the choice.
2. Specify one or more files to change timestamps of, with each file separated by a "|".
3. Proceed with the change when prompted. The current timestamps of the file will be displayed.
4. Proceed with the desired timestamps when prompted.

![Change Timestamp](images/change-timestamp.png)

#### Option Six (Exit)

1. Enter "6" as the choice. Program simply exits without doing anything.

## Authors

- Ng Wei Liang

- Koh Cheng Kiat

- Jovian Ng

- Liew Jwo Young

 
