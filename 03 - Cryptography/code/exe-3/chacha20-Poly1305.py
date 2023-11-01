from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json

try:

	textoPlano = bytes('KeepCoding es una gran oportunidad de aprender muchas cosas sobre ciberseguridad', 'UTF-8')

	clave = bytes.fromhex('c936108299307d3f6f7585b96013346d043f3920b03284c6b45253fd51a545ca')

	nonce_mensaje = get_random_bytes(12)

	datos_asociados = bytes('Datos no cifrados sólo autenticados', 'utf-8')
	cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
	cipher.update(datos_asociados)
	texto_cifrado, tag = cipher.encrypt_and_digest(textoPlano)
  
	mensaje_enviado = { "nonce": b64encode(nonce_mensaje).decode(),"datos asociados": b64encode(datos_asociados).decode(), "texto cifrado": b64encode(texto_cifrado).decode(), "tag": b64encode(tag).decode()}
	print("Mensaje: ", mensaje_enviado)

except (ValueError, KeyError) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error)