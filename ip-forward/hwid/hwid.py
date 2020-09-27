import subprocess, hashlib
from getpass import getpass

def get():
    return str(subprocess.check_output('wmic csproduct get IdentifyingNumber, UUID'))

### NOTE : BIOS ID <Spasi> UUID

print("Getting hwid info..")
hwid = get().split("\\r\\r\\n")[1].split()
print('HWID 1 :', hwid[0])
print('HWID 2 :', hwid[1])
print('Encrypting the hwid')
hashedid = hashlib.sha512(bytes(hwid[0]+ hwid[1] + ".Encrypted.Unhashable.BbayuGt", "utf-8")).hexdigest()
open('hwid.txt', 'w').write(hashedid)
print("Your hashed HWID is saved to hwid.txt! send the hash/file to bbayugt!")
