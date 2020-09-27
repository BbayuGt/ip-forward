import hashlib
password = input('text : ')
password = hashlib.sha256(bytes(password+'bgtunhashable', encoding='utf-8')).hexdigest()
print(password)
input()
