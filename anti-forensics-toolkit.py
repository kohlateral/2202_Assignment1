from Anti_Forensics_Toolkit import secure_delete as sd
from Anti_Forensics_Toolkit import forensic_USB_artifact_shredder as fuas
from Anti_Forensics_Toolkit import forensic_file_artifact_shredder as ffoas
from Anti_Forensics_Toolkit import forensic_account_usage_artifact_shredder as fauas
from Anti_Forensics_Toolkit import time_stamp_manipulation as tsm
import sys
import os

def menu():
    print("WARNING: This program will permanently delete/modify files you specify.")
    print("1. Secure Delete")
    print("2. Delete file opening artifacts")
    print("3. Delete USB Registry Key Identification")
    print("4. Delete Account Usage Artifacts")
    print("5. Modify timestamps")
    print("6. Exit")
    choice = input("Enter choice: ")
    try:
        if choice == "1":
            file_path = input("Enter absolute file path: ")
            confirm = input("Proceed with secure delete of " + file_path + "? (y/n) ").rstrip().lower()
            if confirm == "y":
                sd.secure_delete(file_path)
                print("File Deleted\n")
                menu()
            else:
                menu()
        elif choice == "2":
            confirm = input("Proceed with secure delete of file opening artifacts? (y/n) ").rstrip().lower()
            if confirm == "y":
                ffoas.delete_file_opening_artifacts()
                print("File opening artifacts Deleted\n")
                menu()
            else:
                menu()
            menu()
        elif choice == "3":
            confirm = input("Proceed with secure delete of USB history? (y/n) ").rstrip().lower()
            if confirm == "y":
                fuas.delete_usb_history()
                print("USB history Deleted\n")
                menu()
            else:
                menu()
            menu()
        elif choice == "4":
            confirm = input("Proceed with secure delete of account usage? (y/n) ").rstrip().lower()
            if confirm == "y":
                fauas.delete_account_usage_artifacts()
                print("Account usage Deleted\n")
                menu()
            else:
                menu()
            menu()
        
        elif choice == "5":

            # Use | as the delimiter because it is one of the few characters that will not appear in an absolute path.
            # If a comma is used as a delimiter and a path happens to have a comma, it would be processed incorrectly.
            # Let's say there are 3 files: C:\file,1.txt, C:\file2.txt, C:\file3.txt
            # In this case, there will be 4 items processed instead of 3: C:\file, C:\1.txt, C:\file2.txt, C:\file3.txt
            # Since | is guruanteed to not be in an absolute path, it is safe to use as a delimiter.
            
            file_path_list = list(input("Enter absolute file path(s) (separated by |): ").split("|"))
            confirm = input("Proceed with changing the timestamps? (y/n) ").rstrip().lower()
            
            if confirm == "y":
                for file_path in file_path_list:
                    if os.path.isfile(file_path): # Check if each item in the list is an existing file.
                        tsm.change_timestamp(file_path)
                    else:
                        print(file_path, "is not an existing file and will not be processed.")
                
                print("All files have been processed. Returning to menu...")
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
    menu()


if __name__ == '__main__':
    main()

