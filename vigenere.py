alfabeto = "abcdefghijklmnopqrstuvwxyz"
def cifrado_vigenere(texto, clave):
    texto_cifrado = ""
    i=0
    for letra in texto:
        suma_vigenere = alfabeto.find(letra) + alfabeto.find(clave [i % len(clave)] )
        modulo_abecedario = suma_vigenere % len(alfabeto)
        texto_cifrado += alfabeto[modulo_abecedario]
        i += 1

    return texto_cifrado

def descifrado_vigenere(mensaje_cifrado, clave):
    mensaje_cifrado = mensaje_cifrado.lower()
    mensaje_descifrado = ""

    
    if clave != "":
        i = 0
        for letra in mensaje_cifrado:
            if letra in alfabeto:
                resta_vigenere = alfabeto.find(letra) - alfabeto.find(clave[i % len(clave)])
                modulo_abecedario = resta_vigenere % len(alfabeto)
                mensaje_descifrado += alfabeto[modulo_abecedario]
                i += 1
            else:
                mensaje_descifrado += letra
        return mensaje_descifrado

    else:
        with open("rockyou-top100.txt", "r", encoding="latin-1", errors="ignore") as f:
            for posible_clave in f:
                posible_clave = posible_clave.strip().lower()
                mensaje_descifrado = ""
                i = 0
                for letra in mensaje_cifrado:
                    if letra in alfabeto:
                        resta_vigenere = alfabeto.find(letra) - alfabeto.find(posible_clave[i % len(posible_clave)])
                        modulo_abecedario = resta_vigenere % len(alfabeto)
                        mensaje_descifrado += alfabeto[modulo_abecedario]
                        i += 1
                    else:
                        mensaje_descifrado += letra 
                
                print(f"Clave: {posible_clave} → {mensaje_descifrado}")        
                
                
        
        print("No se encontró una clave válida en el diccionario.")
        return None  