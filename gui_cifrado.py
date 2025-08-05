
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from cesar import cesar_cifrar, cesar_descifrar
from vigenere import vigenere_cifrar, vigenere_descifrar

def ejecutar():
    mensaje = entrada_mensaje.get("1.0", tk.END).strip()
    clave = entrada_clave.get().strip()
    metodo = combo_metodo.get()
    accion = combo_accion.get()

    if not mensaje:
        messagebox.showerror("Error", "Ingrese un mensaje")
        return

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
                cesar_descifrar(mensaje)
                return

    elif metodo == "Vigénère":
        if accion == "Cifrar":
            if not clave.isalpha():
                messagebox.showerror("Error", "La clave debe ser una palabra para el cifrado Vigénère")
                return
            resultado = vigenere_cifrar(mensaje, clave)
        else:
            if clave:
                resultado = vigenere_descifrar(mensaje, clave)
            else:
                archivo = filedialog.askopenfilename(title="Selecciona el archivo de diccionario", filetypes=[("Text files", "*.txt")])
                if not archivo:
                    return
                with open(archivo, 'r', encoding='utf-8') as f:
                    diccionario = f.readlines()
                vigenere_descifrar(mensaje, diccionario=diccionario)
                return

    salida_resultado.delete("1.0", tk.END)
    salida_resultado.insert(tk.END, resultado)

# GUI
ventana = tk.Tk()
ventana.title("Cifrado César y Vigénère")
ventana.geometry("500x500")

ttk.Label(ventana, text="Mensaje:").pack()
entrada_mensaje = tk.Text(ventana, height=5)
entrada_mensaje.pack()

ttk.Label(ventana, text="Clave:").pack()
entrada_clave = ttk.Entry(ventana)
entrada_clave.pack()

ttk.Label(ventana, text="Método:").pack()
combo_metodo = ttk.Combobox(ventana, values=["César", "Vigénère"])
combo_metodo.pack()
combo_metodo.current(0)

ttk.Label(ventana, text="Acción:").pack()
combo_accion = ttk.Combobox(ventana, values=["Cifrar", "Descifrar"])
combo_accion.pack()
combo_accion.current(0)

ttk.Button(ventana, text="Ejecutar", command=ejecutar).pack(pady=10)

ttk.Label(ventana, text="Resultado:").pack()
salida_resultado = tk.Text(ventana, height=10)
salida_resultado.pack()

ventana.mainloop()

