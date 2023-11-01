#!/bin/bash

echo "Ingresa una cadena:"
read cadena

longitud=${#cadena}

resultado=$((longitud / 2))

echo "La cadena está compuesta por $resultado bytes"
