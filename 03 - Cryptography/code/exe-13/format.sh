#!/bin/bash

read -p "Ingresa el nombre de un archivo: " archivo_original; echo

if [ -f "$archivo_original" ]; then

	file1=$(cat "$archivo_original")
	file1_ordenado=$(echo "$file1" | sed -E 's/(.{1,40})/\1\n/g')
	archivo_ordenado="${archivo_original%.*}_ordenado.txt"

	echo -e "$file1_ordenado" > "$archivo_ordenado"; echo
	echo "El contenido del archivo $archivo_original a sido ordenado con exito.";echo
	echo "________________________________________";
	cat "$archivo_ordenado"
	echo "________________________________________"; echo
else
	echo "El archivo $archivo_original no existe."; echo
fi
