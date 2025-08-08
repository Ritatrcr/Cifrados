import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from cesar import cesar_cifrar, cesar_descifrar
from vigenere import cifrado_vigenere, descifrado_vigenere

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def ejecutar():
    mensaje = entrada_mensaje.get("1.0", tk.END).strip()
    clave = entrada_clave.get().strip()
    metodo = combo_metodo.get()
    accion = combo_accion.get()

    if not mensaje:
        messagebox.showerror("Error", "Ingrese un mensaje")
        return

    resultado = ""

    if metodo == "César":
        if accion == "Cifrar":
            if not clave.isdigit():
                messagebox.showerror("Error", "La clave debe ser un número para el cifrado César")
                return
            resultado = cesar_cifrar(mensaje, int(clave))

        else:
            if clave:
                if not clave.isdigit():
                    messagebox.showerror("Error", "La clave debe ser un número para el descifrado César")
                    return
                resultado = cesar_descifrar(mensaje, int(clave))
            else:
                salida_resultado.delete("1.0", tk.END)
                salida_resultado.insert(tk.END, "Fuerza bruta activada:\n\n")
                for k in range(1, 26):
                    resultado = cesar_cifrar(mensaje, -k)
                    salida_resultado.insert(tk.END, f"Clave {k}: {resultado}\n")
                return

    elif metodo == "Vigénère":
        if accion == "Cifrar":
            if not clave.isalpha():
                messagebox.showerror("Error", "La clave debe ser una palabra para el cifrado Vigénère")
                return
            resultado = cifrado_vigenere(mensaje.lower(), clave.lower())

        else:
            if clave:
                resultado = descifrado_vigenere(mensaje.lower(), clave.lower())
            else:
                salida_resultado.delete("1.0", tk.END)
                salida_resultado.insert(tk.END, "Buscando clave con diccionario rockyou-top100.txt...\n\n")
                try:
                    with open("rockyou-top100.txt", "r", encoding="latin-1", errors="ignore") as f:
                        for posible_clave in f:
                            posible_clave = posible_clave.strip().lower()
                            texto = ""
                            i = 0
                            for letra in mensaje.lower():
                                if letra in alfabeto:
                                    resta = alfabeto.find(letra) - alfabeto.find(posible_clave[i % len(posible_clave)])
                                    texto += alfabeto[resta % len(alfabeto)]
                                    i += 1
                                else:
                                    texto += letra
                            salida_resultado.insert(tk.END, f"Clave: {posible_clave} → {texto}\n")
                    return
                except FileNotFoundError:
                    messagebox.showerror("Error", "Archivo rockyou-top100.txt no encontrado.")
                    return

    salida_resultado.delete("1.0", tk.END)
    salida_resultado.insert(tk.END, resultado)


# Alfabeto global para uso en el diccionario
alfabeto = "abcdefghijklmnopqrstuvwxyz"

# Crear ventana principal
ventana = tk.Tk()
ventana.title("🔐 Cifrado César & Vigénère")
ventana.geometry("700x600")
ventana.configure(bg="#f0f4f7")

# Estilo moderno
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11), padding=6)
style.configure("TCombobox", font=("Segoe UI", 11))
style.configure("TEntry", font=("Segoe UI", 11))

frame_principal = ttk.Frame(ventana, padding=15)
frame_principal.pack(expand=True, fill="both")

# Entrada de mensaje
ttk.Label(frame_principal, text="📝 Mensaje:").pack(anchor="w")
entrada_mensaje = tk.Text(frame_principal, height=5, font=("Courier New", 11))
entrada_mensaje.pack(fill="x", pady=5)

# Entrada de clave
ttk.Label(frame_principal, text="Clave:").pack(anchor="w")
entrada_clave = ttk.Entry(frame_principal)
entrada_clave.pack(fill="x", pady=5)

# Método y acción
ttk.Label(frame_principal, text="Método:").pack(anchor="w")
combo_metodo = ttk.Combobox(frame_principal, values=["César", "Vigénère"], state="readonly")
combo_metodo.pack(fill="x", pady=5)
combo_metodo.current(0)

ttk.Label(frame_principal, text="Acción:").pack(anchor="w")
combo_accion = ttk.Combobox(frame_principal, values=["Cifrar", "Descifrar"], state="readonly")
combo_accion.pack(fill="x", pady=5)
combo_accion.current(0)

# Botón ejecutar
ttk.Button(frame_principal, text="🚀 Ejecutar", command=ejecutar).pack(pady=15)

# Resultado
ttk.Label(frame_principal, text="📤 Resultado:").pack(anchor="w")
frame_resultado = ttk.Frame(frame_principal)
frame_resultado.pack(expand=True, fill="both")

scroll_y = ttk.Scrollbar(frame_resultado, orient="vertical")
salida_resultado = tk.Text(frame_resultado, height=15, yscrollcommand=scroll_y.set, font=("Courier New", 10))
scroll_y.config(command=salida_resultado.yview)
scroll_y.pack(side="right", fill="y")
salida_resultado.pack(side="left", expand=True, fill="both")

ventana.mainloop()