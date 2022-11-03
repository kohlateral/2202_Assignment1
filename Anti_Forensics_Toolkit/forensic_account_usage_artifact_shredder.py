from Anti_Forensics_Toolkit import secure_delete as sd
import os


def delete_last_login():
    """delete last login file"""
    try:
        path = 'C:\\windows\\system32\\config\\SAM'
        # sd.secure_delete(path)
        print("SAM file deleted")
    except FileNotFoundError:
        print("SAM file not found")
    except Exception as e:
        print(e)
    return True


def delete_security_event_logs():
    """delete Security events logs"""
    try:
        # open rdp usage file
        path = 'C:\\System32\\winevt\\logs\\Security.evtx'
        try:
            sd.secure_delete(path)
            print("Security events logs deleted")
        except Exception as e:
            print('error in ' + path + '\n Error is ' + e)
    except Exception as e:
        print(e)
    return True


def delete_account_usage_artifacts():
    """delete account usage artifacts"""
    # delete_last_login()
    # delete_security_event_logs()
    return True
