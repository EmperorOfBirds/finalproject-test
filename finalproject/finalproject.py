## This is a test program that sees if PyCryptodome works!
## https://stackoverflow.com/questions/20852664/python-pycrypto-encrypt-decrypt-text-files-with-aes

from Crypto import Random
from Crypto.Cipher import AES

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".enc", 'wb') as fo:
        fo.write(enc)

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name[:-4], 'wb') as fo:
        fo.write(dec)
        
key = b'\x92Q\xdd\xfe\x16\x1c\x97\xc5\x03\xb8;e\xbb\x14\x86\xee\x9a\xf4\xbc>s\x89\xfcgq \xa5\xfd\x87j\xb4\xf0'

    

## key = os.urandom(16)
## print(f"THIS IS YOUR KEY: {key}")
## print("SAVE IT SOMEWHERE IMPORTANT!")

## encrypt_file('to_enc.txt', key)
## decrypt_file('to_enc.txt.enc', key)
