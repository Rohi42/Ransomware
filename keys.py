from Crypto.PublicKey import RSA

key = RSA.generate(2048)
privateKey = key.export_key()
publicKey = key.publickey().export_key()


with open('private.pem', 'wb') as f:
    f.write(privateKey)


with open('public.pem', 'wb') as f:
    f.write(publicKey)

