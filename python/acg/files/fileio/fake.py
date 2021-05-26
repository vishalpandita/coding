import errno
import os
try:
    f = open("fake.txt",'r')
except OSError as err:
    if err.errno != errno.ENOENT:
        print("File not found")
    elif err.errno != errno.EACCES:
        print(f"[Errno {err.errno} ({errno.errorcode[err.errno]})] {os.strerror(err.errno)}")