#!/bin/bash

texto="Siempre existe más de una forma de hacerlo, y más de una solución válida."
key="A212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB"

hmac=$(echo -n "$textoPlano" | openssl dgst -sha256 -mac HMAC -macopt "hexkey:$key" -binary | xxd -p | tr -d '\n')

echo "El HMAC256 del texto ingresado es:"
echo "$hmac"
