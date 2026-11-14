def analizar_secuencia(numero):
    suma=0
    while numero != 1:
        if numero % 2 == 0:
            numero //= 2
            suma += 1
        else:
            numero = 3 * numero + 1
            suma += 1
    return suma + 1

suma = 0
numero_grande = 0
for numero in range(1, 1000000):
    analizado = analizar_secuencia(numero)
    if analizado > suma:
        numero_grande = numero
        suma = analizado

print("El número", numero_grande, "tiene la secuencia más larga con una longitud de", suma, "pasos.")
