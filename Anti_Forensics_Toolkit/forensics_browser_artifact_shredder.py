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
            pass
        print("Chrome history deleted")
    except FileNotFoundError:
        print("Chrome history not found")
    except Exception as e:
        pass
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
                pass
        print("Firefox cookies deleted")
    except FileNotFoundError:
        print("Firefox cookies not found")
    except Exception as e:
        pass
    return True


def delete_chrome_cookies():
    """Delete chrome cookies"""
    try:
        # open chrome cookies
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\'
        files = os.listdir(path)
        for file in files:
            try:
                sd.secure_delete(path + file)
            except Exception as e:
                pass
        print("Chrome cookies deleted")
    except FileNotFoundError:
        print("Chrome cookies not found")
    except Exception as e:
        pass

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
                pass
        print("Firefox history deleted")
    except FileNotFoundError:
        print("Firefox history not found")
    except Exception as e:
        pass
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
                            sd.secure_delete(new_path + cache_file)
                        except Exception as e:
                            pass
            except Exception as e:
                pass
        print("Firefox cache deleted")
    except FileNotFoundError:
        print("Firefox cache not found")
    except Exception as e:
        pass
    return True


def delete_chrome_cache():
    """Delete chrome cache"""
    try:
        # open chrome history
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache\\Cache_Data\\'
        files = os.listdir(path)
        for file in files:
            try:
                sd.secure_delete(path + file)
            except Exception as e:
                pass
        print("Chrome cache deleted")
    except FileNotFoundError:
        print("Chrome cache not found")
    except Exception as e:
        pass
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
