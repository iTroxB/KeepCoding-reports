#!/bin/bash

read -p " -> Enter the string: " clave_aes; echo

hash=$(echo -n "$clave_aes" | xxd -r -p | openssl dgst -sha256 -hex | awk '{print $NF}')
kcv_sha256=${hash:0:6}

echo -n " [+] SHA256 is       : $hash"; echo
echo -n " [+] KCV(SHA-256) is : $kcv_sha256"; echo