from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
import os
import ed25519


#Recuperamos la clave privada RSA
my_path = os.path.abspath(os.getcwd())
path_file_priv = my_path + "/clave-rsa-oaep-priv.pem"


#Guardamos clave y mensaje en bytes
key = RSA.importKey(open(path_file_priv).read())
msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')


#Configuramos y firmamos el texto, luego imprimimos en Hexadecimal
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(key)
signature = signer.sign(hash)
print("Firma PKCS#1 v1.5 en Hexadecimal:", signature.hex())


#Ahora recuperamos clave privada ed25519
privatekey = open("ed25519-priv","rb").read()

#configuramos, guardamos mensaje en bytes, firmamos y imprimimos en Hexadecimal
signedKey = ed25519.SigningKey(privatekey)
msg = bytes('El equipo está preparado para seguir con el proceso, necesitaremos más recursos.','utf8')
signature = signedKey.sign(msg, encoding='hex')
print("Firma ed25519 en Hexadecimal:", signature.hex())
