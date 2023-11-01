#!/bin/bash

read -p "-> Enter first value in hex: " componente1; echo
read -p "-> Enter second value in hex: " componente2; echo

resultado=""
for ((i=0; i<${#componente1}; i++)); do
	byte1="${componente1:i:1}"
	byte2="${componente2:i:1}"

	xor_result=$((16#${byte1} ^ 16#${byte2}))

	resultado="${resultado}$(printf "%X" "$xor_result")"
done

echo "[+] The xor value is: $resultado"
