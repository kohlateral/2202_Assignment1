import os

from Anti_Forensics_Toolkit import secure_delete as sd


def delete_chrome_history():
    """Delete chrome browser history"""
    try:
        # open chrome history
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
        if (os.path.isfile(path)):
            sd.secure_delete(path)
            print("Chrome history deleted")
        else:
            print("Chrome history not found")
            return False
        
    except Exception as e:
        pass
    return True


def delete_firefox_cookies():
    """Delete firefox cookies"""
    try:
        # open firefox cookies
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\'
        profiles = os.listdir(path)
        for profile in profiles:
            try:
                if profile.endswith('.default-release'):
                    full_path = path + profile + '\\cookies.sqlite'
                    if (os.path.isfile(full_path)):
                        sd.secure_delete(full_path)
                        print("Firefox cookies deleted")
                    else:
                        print("Firefox cookies not found")
                        return False
            except Exception as e:
                pass
        
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

        if len(files) == 0:
            print("Chrome cookies not found")
            return False

        for file in files:
            try:
                sd.secure_delete(path + file)
            except Exception as e:
                pass
        print("Chrome cookies deleted")
        
    except Exception as e:
        pass

    return True



def delete_firefox_history():
    """Delete firefox history"""
    try:
        # open firefox history
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\'
        profiles = os.listdir(path)
        
        for profile in profiles:
            try:
                if profile.endswith('.default-release'):
                    full_path = path + profile + '\\places.sqlite'
                    if (os.path.isfile(full_path)):
                        sd.secure_delete(full_path)
                        print("Firefox history deleted")
                    else:
                        print("Firefox history not found")
                        return False

            except Exception as e:
                pass
        
    except Exception as e:
        pass
    return True


def delete_firefox_cache():
    """Delete firefox cache"""
    try:
        # open firefox history
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\'
        profiles = os.listdir(path)
        for profile in profiles:
            try:
                if profile.endswith('.default-release'):
                    new_path = path + profile + '\\cache2\\entries\\'
                    cache_files = os.listdir(new_path)
                    if len(cache_files) == 0:
                        print("Firefox cache not found")
                        return False

                    for cache_file in cache_files:
                        try:
                            sd.secure_delete(new_path + cache_file)
                        except Exception as e:
                            pass
                    print("Firefox cache deleted")
            except Exception as e:
                pass

    except Exception as e:
        pass
    return True


def delete_chrome_cache():
    """Delete chrome cache"""
    try:
        # open chrome history
        userprofile = os.environ['USERPROFILE']
        path = userprofile + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache\\Cache_Data\\'
        cache_files = os.listdir(path)

        if len(cache_files) == 0:
            print("Chrome cache not found")
            return False
        
        for cache_file in cache_files:
            try:
                sd.secure_delete(path + cache_file)
            except Exception as e:
                pass
        print("Chrome cache deleted")
        
    except Exception as e:
        pass
    return True


def delete_browser_artifacts():
    """delete browser artifacts"""
    deleted1 = delete_firefox_cookies()
    deleted2 = delete_chrome_cookies()
    deleted3 = delete_firefox_history()
    deleted4 = delete_chrome_history()
    deleted5 = delete_firefox_cache()
    deleted6 = delete_chrome_cache()

    # If not a single browser artifact is deleted, return False.
    if not deleted1 and not deleted2 and not deleted3 and not deleted4 and not deleted5 and not deleted6:
        return False
    # If at least one browser artifact is deleted, return True.
    else:
        return True
