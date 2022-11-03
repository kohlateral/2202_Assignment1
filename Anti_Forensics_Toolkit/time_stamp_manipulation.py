import os
import datetime
import time
from win32_setfiletime import setctime, setmtime, setatime

def getmtime(file_path):
    """Return the last modification time of a file"""
    modification_time_epoch = os.stat(file_path).st_mtime
    modification_time = datetime.datetime.fromtimestamp(modification_time_epoch).strftime('%d-%m-%Y %H:%M:%S')
    return modification_time

def getatime(file_path):
    """Return the last access time of a file"""
    last_access_time_epoch = os.stat(file_path).st_atime
    last_access_time = datetime.datetime.fromtimestamp(last_access_time_epoch).strftime('%d-%m-%Y %H:%M:%S')
    return last_access_time

def getctime(file_path):
    """Return the creation time of a file"""
    creation_time_epoch = os.stat(file_path).st_ctime
    creation_time = datetime.datetime.fromtimestamp(creation_time_epoch).strftime('%d-%m-%Y %H:%M:%S')
    return creation_time

def change_timestamp(file_path):
    """Modfiy the timestamp for a single file."""
    title = "Target File: " + file_path
    print("-" * len(title))
    print(title)
    print("-" * len(title))

    # Original MAC times
    creation_time = getctime(file_path)
    last_access_time = getatime(file_path)
    modification_time = getmtime(file_path)

    print("Creation Time: ", creation_time)
    print("Last Access Time: ", last_access_time)
    print("Modification Time: ",modification_time)

    # Start of "Change Creation Time"
    creation_time_confirm = ""
    changed_creation_time_epoch = ""
    while not creation_time_confirm== "n" and not creation_time_confirm=="y":
        creation_time_confirm = input("\nChange Creation Time (Y/N)?").rstrip().lower()
        if creation_time_confirm == "y":
            while True:
                changed_creation_time = input("Enter New Creation Time (DD-MM-YYYY HH:MM:SS):")
                try:
                    changed_creation_time_epoch = time.mktime(time.strptime(changed_creation_time, '%d-%m-%Y %H:%M:%S'))
                except ValueError as e:
                    print("Invalid format!")
                else:
                    setctime(file_path, changed_creation_time_epoch)
                    print("New Creation Time: ", getctime(file_path))
                    break

        elif creation_time_confirm == "n" :
            print("Creation Time will not be changed. Skipping...\n")
            break

        else:
            continue
    # End of "Change Creation Time"

    # Start of "Change Last Access Time"
    last_access_time_confirm = ""
    changed_last_access_time_epoch = ""

    while not last_access_time_confirm== "n" and not last_access_time_confirm=="y":
        last_access_time_confirm = input("\nChange Last Access Time (Y/N)?").rstrip().lower()
        if last_access_time_confirm == "y":
            while True:
                changed_last_access_time = input("Enter New Last Access Time (DD-MM-YYYY HH:MM:SS):")
                try:
                    changed_last_access_time_epoch = time.mktime(time.strptime(changed_last_access_time, '%d-%m-%Y %H:%M:%S'))
                except ValueError:
                    print("Invalid format!")
                else:
                    setatime(file_path, changed_last_access_time_epoch)
                    print("New Last Access Time: ", getatime(file_path))
                    break

        elif last_access_time_confirm == "n" :
            print("Last Access Time will not be changed. Skipping...\n")
            break

        else:
            continue
    # End of "Change Last Access Time"

    # Start of "Change Modification Time"
    modification_time_confirm = ""
    changed_modification_time_epoch = ""

    while not modification_time_confirm== "n" and not modification_time_confirm=="y":
        modification_time_confirm = input("\nChange Modification Time (Y/N)?").rstrip().lower()
        if modification_time_confirm == "y":
            while True:
                changed_modification_time = input("Enter New Modification Time (DD-MM-YYYY HH:MM:SS):")
                try:
                    changed_modification_time_epoch = time.mktime(time.strptime(changed_modification_time, '%d-%m-%Y %H:%M:%S'))
                except ValueError:
                    print("Invalid format!")
                else:
                    setmtime(file_path, changed_modification_time_epoch)
                    print("New Modification Time: ", getmtime(file_path))
                    break

        elif modification_time_confirm == "n" :
            print("Modification Time will not be changed. Skipping...\n")
            break

        else:
            print("Invalid option!")

    # End of "Change Modification Time"
    