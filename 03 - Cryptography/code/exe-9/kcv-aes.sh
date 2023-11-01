#!/bin/bash

read -p " -> Enter the text: " text
read -p " -> Enter the iv: " iv
read -p " -> Enter the AES key: " key; echo

AES=$(echo -n "$text" | xxd -r -p | openssl enc -aes-256-cbc -K "$key" -iv "$iv" | xxd -p -c 32)
kcv-aes=${AES:0:6}

echo " [+] AES: $AES"; echo
echo " [+] KCV(AES-CBC): $kcv-aes"; echo
