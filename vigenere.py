def vigenere_cifrar(mensaje, clave):
    resultado = ""
    clave_repetida = (clave * (len(mensaje) // len(clave) + 1))[:len(mensaje)]
    for c, k in zip(mensaje, clave_repetida):
        if c.isalpha():
            desplazamiento = ord(k.lower()) - ord('a')
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
        else:
            resultado += c
    return resultado

def vigenere_descifrar(mensaje_cifrado, clave=None, diccionario=None):
    if clave is not None:
        resultado = ""
        clave_repetida = (clave * (len(mensaje_cifrado) // len(clave) + 1))[:len(mensaje_cifrado)]
        for c, k in zip(mensaje_cifrado, clave_repetida):
            if c.isalpha():
                desplazamiento = ord(k.lower()) - ord('a')
                base = ord('A') if c.isupper() else ord('a')
                resultado += chr((ord(c) - base - desplazamiento) % 26 + base)
            else:
                resultado += c
        return resultado
    elif diccionario is not None:
        print("Intentando con diccionario de claves...")
        for k in diccionario:
            intento = vigenere_descifrar(mensaje_cifrado, k.strip())
            print(f"Clave '{k.strip()}': {intento}")




# mensaje = "Hola Mundo"
# clave = "clave"

# cifrado = vigenere_cifrar(mensaje, clave)
# print("Cifrado:", cifrado)

# # Descifrado con clave
# descifrado = vigenere_descifrar(cifrado, clave)
# print("Descifrado:", descifrado)

# # Descifrado sin clave (con diccionario)
# with open('rockyou-top100.txt', 'r', encoding='utf-8') as f:
#     diccionario = f.readlines()
# vigenere_descifrar(cifrado, diccionario=diccionario)

