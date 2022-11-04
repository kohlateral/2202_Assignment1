from Anti_Forensics_Toolkit import secure_delete as sd
from Anti_Forensics_Toolkit import forensic_USB_artifact_shredder as fuas
from Anti_Forensics_Toolkit import forensic_file_artifact_shredder as ffoas
from Anti_Forensics_Toolkit import forensics_browser_artifact_shredder as fbas
from Anti_Forensics_Toolkit import time_stamp_manipulation as tsm

import sys
import ctypes
import os

def is_admin():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def menu():
    print("\nWARNING: Anti-Forensics Toolkit will permanently delete/modify files you specify.")
    print("1. Secure Delete")
    print("2. Delete file opening artifacts")
    print("3. Delete USB Registry Key Identification")
    print("4. Delete Browser Artifacts")
    print("5. Change timestamps")
    print("6. Exit")
    choice = input("Enter choice: ")    
    try:
        if choice == "1":
            # Use | as the delimiter because it is one of the few characters that will not appear in an absolute path.
            file_path_list = list(input("Enter absolute file path(s) (separated by |): ").split("|"))
            confirm = input("Proceed with secure delete? (y/n) ").rstrip().lower()

            if confirm == "y":
                for file_path in file_path_list:
                    if os.path.isfile(file_path):  # Check if each item in the list is an existing file.
                        sd.secure_delete(file_path)
                        print(file_path, "deleted")
                    else:
                        print(file_path, "is not an existing file and will not be processed.")

                print("\nAll files have been deleted. Returning to menu...")
                menu()
            else:
                menu()

        elif choice == "2":
            confirm = input("Proceed with secure delete of file opening artifacts? (y/n) ").rstrip().lower()
            if confirm == "y":
                ffoas.delete_file_opening_artifacts()
                print("\nFile opening artifacts Deleted. Returning to menu...")
                menu()
            else:
                menu()
            menu()
        elif choice == "3":
            confirm = input("Proceed with secure delete of USB history? (y/n) ").rstrip().lower()
            if confirm == "y":
                fuas.delete_usb_history()
                print("\nUSB history Deleted. Returning to menu...")
                menu()
            else:
                menu()
            menu()

        elif choice == "4":
            confirm = input("Proceed with secure delete of browser artifacts? (y/n) ").rstrip().lower()
            if confirm == "y":
                fbas.delete_browser_artifacts()
                print("\nBrowser Artifacts Deleted. Returning to menu...")
                menu()
            else:
                menu()
            menu()

        elif choice == "5":
            # Use | as the delimiter because it is one of the few characters that will not appear in an absolute path.
            file_path_list = list(input("Enter absolute file path(s) (separated by |): ").split("|"))
            confirm = input("Proceed with changing the timestamps? (y/n) ").rstrip().lower()

            if confirm == "y":
                for file_path in file_path_list:
                    if os.path.isfile(file_path):  # Check if each item in the list is an existing file.
                        tsm.change_timestamp(file_path)
                    else:
                        print(file_path, "is not an existing file. Skipping...")
                print("\nAll files have been processed. Returning to menu...")
                menu()
            else:
                menu()

        elif choice == "6":
            sys.exit()

        else:
            print("Invalid choice\n")
            menu()
    except Exception as e:
        return e


def main():
    if not is_admin():
        print("Please run as administrator!")
    else:
        menu()


if __name__ == '__main__':
    main()