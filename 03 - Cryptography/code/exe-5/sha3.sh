#!/bin/bash

# Cadena 1: texto sin punto final
cadena1="En KeepCoding aprendemos cómo protegernos con criptografía"
# Cadena 2: texto con punto final
cadena2="En KeepCoding aprendemos cómo protegernos con criptografía."

hash_cadena1=$(echo -n "$cadena1" | openssl dgst -sha3-256 | awk '{print $NF}')
hash_cadena2=$(echo -n "$cadena2" | openssl dgst -sha3-256 | awk '{print $NF}')

echo "Cadena 1: $cadena1"
echo "Hash SHA3-256: $hash_cadena1"
echo

echo "Cadena 2: $cadena2"
echo "Hash SHA3-256: $hash_cadena2"
