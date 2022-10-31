from Anti_Forensics_Toolkit import secure_delete as sd
from Anti_Forensics_Toolkit import forensic_artifact_shredder as fas
import sys


def menu():
    print("WARNING: This program will permanently delete files you specify.")
    print("1. Secure Delete")
    print("2. Delete Prefetch Files")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        file_path = input("Enter absolute file path: ")
        confirm = input("Proceed with secure delete of " + file_path + "? (y/n)\n")
        if confirm == "y":
            sd.secure_delete(file_path)
            print("File Deleted\n")
            menu()
        else:
            menu()
    elif choice == "2":
        confirm = input("Proceed with secure delete of prefetch files? (y/n)\n")
        if confirm == "y":
            fas.delete_prefetch_files()
            print("Prefetch Files Deleted\n")
            menu()
        else:
            menu()
        menu()
    elif choice == "3":
        sys.exit()
    else:
        print("Invalid choice\n")
        menu()


def main():
    menu()


if __name__ == '__main__':
    main()

