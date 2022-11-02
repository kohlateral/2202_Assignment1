from Anti_Forensics_Toolkit import secure_delete as sd
import winreg


def delete_registry_key_securely(key):
    """delete registry key securely"""
    # open registry key
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key)
        # print all subkeys
        for i in range(0, winreg.QueryInfoKey(reg_key)[0]):
            subkey_name = winreg.EnumKey(reg_key, i)
            print(subkey_name)
            # delete subkey
            # winreg.DeleteKey(reg_key, subkey_name)
    except FileNotFoundError:
        print("Registry key not found")
    except Exception as e:
        print(e)
    return True


def delete_usb_registry_key_identification():
    """delete usb registry key identification"""
    # open registry key
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Enum\USBSTOR",
                                 0, winreg.KEY_ALL_ACCESS)
        # print all subkeys
        for i in range(0, winreg.QueryInfoKey(reg_key)[0]):
            subkey_name = winreg.EnumKey(reg_key, i)
            print(subkey_name)
            # delete subkey
            try:
                winreg.DeleteKey(reg_key, subkey_name)
            except Exception as e:
                print(e)
            print('TODO: delete USBSTOR subkey')
    except FileNotFoundError:
        print("Registry key USBSTOR not found")
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Enum\USB",
                                 0, winreg.KEY_ALL_ACCESS)
        # print all subkeys
        for i in range(0, winreg.QueryInfoKey(reg_key)[0]):
            subkey_name = winreg.EnumKey(reg_key, i)
            print(subkey_name)
            # delete subkey
            try:
                winreg.DeleteKey(reg_key, subkey_name)
            except Exception as e:
                print(e)
            print('TODO: delete USB subkey')
    except FileNotFoundError:
        print("Registry key USB not found")
    except Exception as e:
        print(e)
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
        # print all keys
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
        # open Plug and Play Log Files
        path = 'C:\\Windows\\System32\\winevt\\Logs\\System.evtx'
        print("File found")
        sd.secure_delete(path)
    except FileNotFoundError:
        print("Plug and Play Log Files not found")
    except Exception as e:
        print(e)
    return True


def delete_usb_history():
    """delete usb history"""
    delete_usb_registry_key_identification()
    delete_first_last_usb_times()
    delete_user_usb_information()
    delete_pnp_events()
    return True
