def cesar_cifrar(mensaje, clave):
    resultado = ""
    for c in mensaje:
        if c.isalpha():
            desplazado = ord(c) + clave
            if c.isupper():
                resultado += chr((desplazado - 65) % 26 + 65)
            else:
                resultado += chr((desplazado - 97) % 26 + 97)
        else:
            resultado += c
    return resultado

def cesar_descifrar(mensaje_cifrado, clave=None):
    if clave is not None:
        return cesar_cifrar(mensaje_cifrado, -clave)
    else:
        print("Fuerza bruta activada. Probando todas las claves posibles:")
        for k in range(1, 26):
            print(f"Clave {k}: {cesar_cifrar(mensaje_cifrado, -k)}")



# mensaje = "Hola Mundo"
# clave = 3

# cifrado = cesar_cifrar(mensaje, clave)
# print("Cifrado:", cifrado)

# # Descifrado con clave
# descifrado = cesar_descifrar(cifrado, clave)
# print("Descifrado:", descifrado)

# # Descifrado sin clave (fuerza bruta)
# cesar_descifrar(cifrado)
