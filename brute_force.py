# brute_force.py
import pyzipper, itertools, string
def crack_zip(file, chars, length):
    with pyzipper.AESZipFile(file) as zf:
        for attempt in itertools.product(chars, repeat=length):
            pwd = "".join(attempt)
            try:
                zf.extractall(pwd=pwd.encode())
                return pwd
            except: continue
