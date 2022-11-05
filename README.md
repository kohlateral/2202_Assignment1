# Anti-Forensics Toolkit (User Manual)

Anti-Forensics Toolkit aims to securely delete selected files, securely delete known forensic artifacts, and manipulate timestamps of selected files.

## Table Of Contents

- [Anti-Forensics Toolkit (User Manual)](#anti-forensics-toolkit-user-manual)
  * [Table Of Contents](#table-of-contents)
  * [Getting Started](#getting-started)
    + [Requirements](#requirements)
    + [Libraries](#libraries)
    + [Executing program](#executing-program)
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


#### Option One

1. Specify one or more files to securely delete, with each file separated by a "|".
2. Proceed with the deletion when prompted.

![Secure Delete](images/secure-delete.png)

#### Option Two

1. 

#### Option Three

#### Option Four

#### Option Five

1. Specify one or more files to change timestamps of, with each file separated by a "|".
2. Proceed with the change when prompted.
3. The current timestamps of the file will be displayed.

![Change Timestamp 1](images/change-timestamp-1.png)

4. Proceed with changing one or more timestamps when prompted.

![Change Timestamp 2](images/change-timestamp-2.png))

#### Option Six

- Simply exit without doing anything.

## Authors

- Ng Wei Liang

- Koh Cheng Kiat

- Jovian Ng

- Liew Jwo Young

 
