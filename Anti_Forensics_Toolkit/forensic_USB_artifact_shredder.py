import os

from Anti_Forensics_Toolkit import secure_delete as sd
import winreg


zero_REG_SZ_value = '00' * 4096
zero_REG_DWORD_value = 0 * 4096
zero_REG_MULTI_SZ_value = ['00' * 4096]


def overwrite_usb_registry_key_identification():
    """delete usb registry key identification"""
    # open registry key
    list_of_devices = []
    list_of_serial_numbers = []

    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Enum\USBSTOR",
                                 0, winreg.KEY_ALL_ACCESS)
        # print all subkeys
        for i in range(0, winreg.QueryInfoKey(reg_key)[0]):
            device = winreg.EnumKey(reg_key, i)
            list_of_devices.append(device)
            print(device)
            # list all subkeys
            for device in list_of_devices:
                subkey = r"SYSTEM\CurrentControlSet\Enum\USBSTOR" + "\\" + device
                open_subkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey, 0, winreg.KEY_ALL_ACCESS)
                for j in range(0, winreg.QueryInfoKey(open_subkey)[0]):
                    serial_number = winreg.EnumKey(open_subkey, j)
                    list_of_serial_numbers.append(serial_number)
                # query values
                for serial_number in list_of_serial_numbers:
                    subkey = subkey + "\\" + serial_number
                    open_subkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey, 0, winreg.KEY_ALL_ACCESS)
                    for k in range(0, winreg.QueryInfoKey(open_subkey)[1]):
                        usb_information = winreg.EnumValue(open_subkey, k)
                        try:
                            # if data type is REG_SZ
                            if usb_information[2] == 1:
                                winreg.SetValueEx(open_subkey, usb_information[0], 0,
                                                  usb_information[2], zero_REG_SZ_value)
                            # if data type is REG_DWORD
                            elif usb_information[2] == 4:
                                winreg.SetValueEx(open_subkey, usb_information[0], 0,
                                                  usb_information[2], zero_REG_DWORD_value)
                            # if data type is REG_MULTI_SZ
                            elif usb_information[2] == 7:
                                winreg.SetValueEx(open_subkey, usb_information[0], 0,
                                                  usb_information[2], zero_REG_MULTI_SZ_value)
                        except Exception as e:
                            print('Error ' + usb_information[0] + ' ' + str(e))
            print('Overwritten USBSTOR subkey')
    except FileNotFoundError:
        print("Registry key USBSTOR not found")
    return True


def delete_first_last_usb_times():
    """delete first and last USB times"""
    # open registry key
    try:
        # open Plug and Play Log Files
        path = 'C:\\Windows\\INF\\setupapi.dev.log'
        print("File found")
        sd.secure_delete(path)
    except FileNotFoundError:
        print("Registry key USB not found")
    except Exception as e:
        print(e)
    return True


def delete_user_usb_information():
    """delete user usb information"""
    # open registry key
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\MountedDevices", 0, winreg.KEY_ALL_ACCESS)
        for i in range(0, winreg.QueryInfoKey(reg_key)[1]):
            information = winreg.EnumValue(reg_key, i)
            print(information)
            # delete registry value
            # winreg.DeleteValue(reg_key, information[i])
    except Exception as e:
        print(e)
    return True


def delete_pnp_events():
    """deletes Plug N Play event logs"""
    try:
        # turn off windows event logging
        os.system('auditpol /set /subcategory:"Filtering Platform Connection" /success:disable /failure:disable')
        # open Plug and Play Log Files
        path = 'C:\\Windows\\System32\\winevt\\Logs\\System.evtx'
        sd.secure_delete(path)
    except FileNotFoundError:
        print("Plug and Play Log Files not found")
    except Exception as e:
        print(e)
    return True


def delete_usb_history():
    """delete usb history"""
    overwrite_usb_registry_key_identification()
    delete_first_last_usb_times()
    # delete_user_usb_information()
    # delete_pnp_events()
    return True
