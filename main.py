from Anti_Forensics_Toolkit import secure_delete as sd
from Anti_Forensics_Toolkit import forensic_USB_artifact_shredder as fuas
from Anti_Forensics_Toolkit import forensic_file_artifact_shredder as ffoas
from Anti_Forensics_Toolkit import forensic_account_usage_artifact_shredder as fauas
import sys


def menu():
    print("WARNING: This program will permanently delete files you specify.")
    print("1. Secure Delete")
    print("2. Delete file opening artifacts")
    print("3. Delete USB Registry Key Identification")
    print("4. Delete Account Usage Artifacts")
    print("0. Exit")
    choice = input("Enter choice: ")
    try:
        if choice == "1":
            file_path = input("Enter absolute file path: ")
            confirm = input("Proceed with secure delete of " + file_path + "? (y/n)")
            if confirm == "y":
                sd.secure_delete(file_path)
                print("File Deleted\n")
                menu()
            else:
                menu()
        elif choice == "2":
            confirm = input("Proceed with secure delete of file opening artifacts? (y/n)")
            if confirm == "y":
                ffoas.delete_file_opening_artifacts()
                print("File opening artifacts Deleted\n")
                menu()
            else:
                menu()
            menu()
        elif choice == "3":
            confirm = input("Proceed with secure delete of USB history? (y/n)")
            if confirm == "y":
                fuas.delete_usb_history()
                print("USB history Deleted\n")
                menu()
            else:
                menu()
            menu()
        elif choice == "4":
            confirm = input("Proceed with secure delete of account usage? (y/n)")
            if confirm == "y":
                fauas.delete_account_usage_artifacts()
                print("Account usage Deleted\n")
                menu()
            else:
                menu()
            menu()
        elif choice == "0":
            sys.exit()
        else:
            print("Invalid choice\n")
            menu()
    except Exception as e:
        return e


def main():
    menu()


if __name__ == '__main__':
    main()

