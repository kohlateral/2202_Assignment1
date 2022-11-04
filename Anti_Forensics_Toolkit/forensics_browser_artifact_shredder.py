import os

from Anti_Forensics_Toolkit import secure_delete as sd


def delete_chrome_history():
    """Delete chrome browser history"""
    try:
        # open chrome history
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
        try:
            sd.secure_delete(path)
        except Exception as e:
            print(e)
        print("Chrome history deleted")
    except FileNotFoundError:
        print("Chrome history not found")
    except Exception as e:
        print('error in ' + path + '\n Error is ' + str(e) + '\n')
    return True


def delete_firefox_cookies():
    """Delete firefox cookies"""
    try:
        # open firefox cookies
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\'
        files = os.listdir(path)
        for file in files:
            try:
                if file.endswith('.default-release'):
                    sd.secure_delete(path + file + '\\cookies.sqlite')
            except Exception as e:
                print(e)
        print("Firefox cookies deleted")
    except FileNotFoundError:
        print("Firefox cookies not found")
    except Exception as e:
        print('error in ' + path + '\n Error is ' + str(e) + '\n')
    return True


def delete_chrome_cookies():
    """Delete chrome cookies history"""
    try:
        # open chrome history
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Locale Storage\\LevelDB\\'
        files = os.listdir(path)
        for file in files:
            try:
                sd.secure_delete(file)
            except Exception as e:
                print(e)
        print("Chrome history deleted")
    except FileNotFoundError:
        print("Chrome history not found")
    except Exception as e:
        print('error in ' + path + '\n Error is ' + str(e) + '\n')
    return True


def delete_firefox_history():
    """Delete firefox history"""
    try:
        # open firefox history
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\'
        files = os.listdir(path)
        for file in files:
            try:
                if file.endswith('.default-release'):
                    sd.secure_delete(path + file + '\\places.sqlite')
            except Exception as e:
                print(e)
        print("Firefox history deleted")
    except FileNotFoundError:
        print("Firefox history not found")
    except Exception as e:
        print('error in ' + path + '\n Error is ' + str(e) + '\n')
    return True


def delete_firefox_cache():
    """Delete firefox cache"""
    try:
        # open firefox history
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\'
        files = os.listdir(path)
        for file in files:
            try:
                if file.endswith('.default-release'):
                    new_path = path + file + '\\cache2\\entries\\'
                    cache_files = os.listdir(new_path)
                    for cache_file in cache_files:
                        try:
                            sd.secure_delete(cache_file)
                        except Exception as e:
                            print(e)
            except Exception as e:
                print(e)
        print("Firefox cache deleted")
    except FileNotFoundError:
        print("Firefox cache not found")
    except Exception as e:
        print('error in ' + path + '\n Error is ' + str(e) + '\n')
    return True


def delete_chrome_cache():
    """Delete chrome cache"""
    try:
        # open chrome history
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache\\Cache-Data'
        files = os.listdir(path)
        for file in files:
            try:
                sd.secure_delete(file)
            except Exception as e:
                print(e)
        print("Chrome cache deleted")
    except FileNotFoundError:
        print("Chrome cache not found")
    except Exception as e:
        print('error in ' + path + '\n Error is ' + str(e) + '\n')
    return True


def delete_browser_artifacts():
    """delete browser artifacts"""
    delete_firefox_cookies()
    delete_chrome_cookies()
    delete_firefox_history()
    delete_chrome_history()
    delete_firefox_cache()
    delete_chrome_cache()
    return True
