import os

cluster_size = 4096


def secure_delete(file_path):
    """Securely delete file by overwriting with 7 passes of data."""
    try:
        # pass one
        write_zeros(file_path)
        # pass two
        write_one(file_path)
        # pass three
        write_random(file_path)
        # pass four
        write_random(file_path)
        # pass five
        write_zeros(file_path)
        # pass six
        write_one(file_path)
        # pass seven
        write_random(file_path)
        # rename file name 20 times
        new_file_name = rename_file(file_path)
        # delete file
        os.remove(new_file_name)
    except Exception as e:
        return False
    return True


def write_zeros(file_path):
    """open file and overwrite with zeros"""
    with open(file_path, 'wb') as f:
        f.seek(0)
        write_bytes = 0
        while write_bytes < os.path.getsize(file_path):
            f.write(b'\x00' * cluster_size)
            write_bytes += cluster_size
        f.flush()
        fd = f.fileno()
        os.fsync(fd)
    return True


def write_one(file_path):
    """open file and overwrite with ones"""
    with open(file_path, 'wb') as f:
        f.seek(0)
        write_bytes = 0
        while write_bytes < os.path.getsize(file_path):
            f.write(b'\xFF' * cluster_size)
            write_bytes += cluster_size
        f.flush()
        fd = f.fileno()
        os.fsync(fd)
    return True


def write_random(file_path):
    """open file and overwrite with random data"""
    with open(file_path, 'wb') as f:
        f.seek(0)
        f.write(os.urandom(os.path.getsize(file_path)))
        write_bytes = 0
        while write_bytes < os.path.getsize(file_path):
            f.write(os.urandom(2 * cluster_size))
            write_bytes += cluster_size
        f.flush()
        fd = f.fileno()
        os.fsync(fd)
    return True


def rename_file(file_path):
    """Rename file to random string 20 times."""
    for i in range(20):
        new_name = os.urandom(16).hex()
        os.rename(file_path, new_name)
        file_path = new_name
    return new_name


def enable_ssd_trim():
    """Enable trim on Windows using fsutil."""
    os.system('fsutil behavior set disabledeletenotify 0')
    return True
