from Anti_Forensics_Toolkit import secure_delete as sd
import os


def delete_prefetch_files():
    """securely delete prefetch files"""
    try:
        # open prefetch files
        path = 'C:\\Windows\\Prefetch\\'
        # list all files in directory
        files = os.listdir(path)
        # iterate through files
        for file in files:
            # check if file is a prefetch file
            if file.endswith('.pf'):
                # secure delete file
                sd.secure_delete(path + file)
        print("Prefetch files deleted\n")
    except FileNotFoundError:
        print("Prefetch folder not found\n")
    except Exception as e:
        print('error in ' + path + '\n Error is ' + e + '\n')
    return True


def delete_jump_list():
    """delete jump list"""
    try:
        # open jump list
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Roaming\\Microsoft\\Windows\\Recent\\AutomaticDestinations\\'
        files = os.listdir(path)
        for file in files:
            try:
                sd.secure_delete(path + file)
            except Exception as e:
                print(e)
        print("Jump list deleted")
    except FileNotFoundError:
        print("Jump list not found")
    except Exception as e:
        print('error in ' + path + '\n Error is ' + e + '\n')
    return True


def delete_history_file():
    """delete ie edge file"""
    try:
        # open ie edge file
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Local\\Microsoft\\Windows\\History\\History.IE5\\'
        files = os.listdir(path)
        for file in files:
            try:
                sd.secure_delete(path + file)
            except Exception as e:
                print(e)
        print("IE Edge file deleted")
    except FileNotFoundError:
        print("IE Edge file not found")
    except Exception as e:
        print('error in ' + path + '\n Error is ' + e + '\n')
    return True


def delete_thumbcache_db():
    """delete thumbcache db"""
    try:
        # open thumbcache db
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Local\\Microsoft\\Windows\\Explorer\\'
        files = os.listdir(path)
        for file in files:
            try:
                sd.secure_delete(path + file)
            except Exception as e:
                print(e)
        print("Thumbcache db deleted")
    except FileNotFoundError:
        print("Thumbcache db not found")
    except Exception as e:
        print('error in ' + path + '\n Error is ' + e + '\n')
    return True


def delete_outlook_artifacts():
    """delete outlook artifacts"""
    try:
        # open Email Attachments
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Local\\Microsoft\\Outlook\\Explorer\\'
        files = os.listdir(path)
        for file in files:
            try:
                sd.secure_delete(path + file)
            except Exception as e:
                print(e)
        print("outlook artifacts deleted")
    except FileNotFoundError:
        print("outlook artifacts not found")
    except Exception as e:
        print('error in ' + path + '\n Error is ' + e + '\n')
    return True


def delete_file_downloads():
    """delete file downloads"""
    try:
        # open Email Attachments
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Roaming\\Microsoft\\Windows\\IEDownloadHistory\\'
        files = os.listdir(path)
        for file in files:
            try:
                sd.secure_delete(path + file)
            except Exception as e:
                print(e)
        print("outlook artifacts deleted")
    except FileNotFoundError:
        print("outlook artifacts not found")
    except Exception as e:
        print('error in ' + path + '\n Error is ' + e + '\n')
    return True


def delete_amcache_hve():
    """delete amcache hve"""
    try:
        # open amcache hve
        path = 'C:\\Windows\\AppCompat\\Programs\\Amcache.hve'
        try:
            sd.secure_delete(path)
        except Exception as e:
            print(e)
        print("Amcache.hve deleted")
    except FileNotFoundError:
        print("Amcache.hve not found")
    except Exception as e:
        print('error in ' + path + '\n Error is ' + e + '\n')
    return True


def delete_windows_timeline():
    """delete windows timeline"""
    try:
        # open Email Attachments
        user = os.getlogin()
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Local\\ConnectedDevicesPlatform\\L.' + user + '\\ActivitiesCache.db'
        try:
            sd.secure_delete(path)
        except Exception as e:
            print(e)
        print("windows timeline deleted")
    except FileNotFoundError:
        print("windows timeline not found")
    except Exception as e:
        print('error in ' + path + '\n Error is ' + e + '\n')
    return True


def delete_file_opening_artifacts():
    """delete file opening artifacts"""
    delete_prefetch_files()
    delete_jump_list()
    # delete_history_file()
    delete_thumbcache_db()
    delete_outlook_artifacts()
    delete_file_downloads()
    # delete_amcache_hve()
    # delete_windows_timeline()
    return True
