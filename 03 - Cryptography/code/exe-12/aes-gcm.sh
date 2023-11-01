#!/bin/bash

# Clave en formato hexadecimal
clave_hex="E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74"

# Nonce en formato hexadecimal
nonce_hex="9Yccn/f5nJJhAt2S"

# Cadena a cifrar
cadena_a_cifrar="Tu cadena a cifrar aquí"

# Cifrar la cadena utilizando OpenSSL
cadena_cifrada_hex=$(echo -n "$cadena_a_cifrar" | xxd -p | openssl enc -aes-256-gcm -K "$clave_hex" -iv "$nonce_hex" -e -a)

# Imprimir la cadena cifrada
echo "Cadena cifrada en formato base64: $cadena_cifrada_hex"
