from Anti_Forensics_Toolkit import secure_delete as sd
import winreg
import os


def delete_prefetch_files():
    """securely delete prefetch files"""
    # open prefetch files
    path = 'C:\\Windows\\Prefetch'
    # list all files in directory
    files = os.listdir(path)
    # iterate through files
    for file in files:
        # check if file is a prefetch file
        if file.endswith('.pf'):
            # secure delete file
            sd.secure_delete(path + file)
    return True


def delete_usb_registry_key_identification():
    """delete usb registry key identification"""
    # open registry key
    reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Enum\USBSTOR")
    # delete registry key
    winreg.DeleteKey(reg_key, "Device Parameters")
    return True

