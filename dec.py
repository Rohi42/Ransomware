import os
from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES


privateKeyFile = 'private.pem'


def scanRecurse(baseDir):
    
    for entry in os.scandir(baseDir):
        if entry.is_file():
            yield entry
        else:
            yield from scanRecurse(entry.path)


def decrypt(dataFile, privateKeyFile):
    '''
    use EAX mode to allow detection of unauthorized modifications
    '''

    
    extension = dataFile.suffix.lower()
    with open(privateKeyFile, 'rb') as f:
        privateKey = f.read()
        
        key = RSA.import_key(privateKey)

    
    with open(dataFile, 'rb') as f:
        
        encryptedSessionKey, nonce, tag, ciphertext = [ f.read(x) for x in (key.size_in_bytes(), 16, 16, -1) ]

  
    cipher = PKCS1_OAEP.new(key)
    sessionKey = cipher.decrypt(encryptedSessionKey)

    
    cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    
    dataFile = str(dataFile)
    fileName= dataFile.split(extension)[0]
   
    decryptedFile = fileName 
    with open(decryptedFile, 'wb') as f:
        f.write(data)

    print('Decrypted file saved to ' + decryptedFile)

directory = './' 


dir = input('put your directory (default is "./" ):')
if dir:
  directory = dir



includeExtension = ['.encrypted'] 

for item in scanRecurse(directory): 
    filePath = Path(item)
    fileType = filePath.suffix.lower()
   
    if fileType in includeExtension:
      
      decrypt(filePath, privateKeyFile)
