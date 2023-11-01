import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


clave = bytes.fromhex('A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72')
iv_bytes = bytes.fromhex('00000000000000000000000000000000')

try:

	iv_desc_bytes = bytes.fromhex("00000000000000000000000000000000")
	texto_cifrado_bytes = b64decode("TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=")
	cipher = AES.new(clave, AES.MODE_CBC, iv_desc_bytes)

	mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style="x923")
	#mensaje_des_bytes = cipher.decrypt(texto_cifrado_bytes)
	#print(mensaje_des_bytes.hex())
	print(" El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))

except (ValueError, KeyError) as error:
	print('Problemas para descifrar....')
	print("El motivo del error es: ", error)
