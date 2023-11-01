from Crypto.Cipher import ChaCha20
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes

textoPlano_bytes = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')
clave = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
nonce_mensaje = bytes.fromhex('f5871c9ff7f99c926102dd92')

print(' nonce  = ', nonce_mensaje.hex())

cipher = ChaCha20.new(key=clave, nonce=nonce_mensaje)
texto_cifrado = cipher.encrypt(textoPlano_bytes)
print(' Mensaje cifrado en HEX = ', texto_cifrado.hex() )
print(' Mensaje cifrado en B64 = ', b64encode(texto_cifrado).decode('utf-8'))