import pyautogui
import tkinter as tk
from tkinter import*
from tkinter import messagebox, filedialog


#interfaz
def crearWidgets():
    etiquetaGuarar = Label(vn, text = "Guardar como: ", font=("",10, "bold"),bg="blue",fg="white")
    etiquetaGuarar.grid(row=1, column = 0, pady = 5, padx = 5)

    vn.textoGuardar = Entry(vn, width =30)
    vn.textoGuardar.grid(row=1, column =1, pady = 5, padx = 5)

    botonGuardar = Button(vn, text = "Navegar", width=10, command=navegar)
    botonGuardar.grid(row=1, column =2, pady = 5, padx = 5)

    botonCaptura = Button(vn, text = "Captura", width=10, command=captura)
    botonCaptura.grid(row=2, column=1, pady = 5,padx = 5)

#funcion para navegar y guardar la imagen

def navegar():
    vn.archivoNombre = filedialog.asksaveasfilename(title = "Guardar como",
                                                    initialdir="C:\\Users\\luisc\\desktop",
                                                    defaultextension=".png",
                                                    filetypes=(("Archivo Png","*.png"),("Todos Archivos","*")))
    vn.textoGuardar.insert("1", vn.archivoNombre)

#captura de pantalla

def captura():
    captura = pyautogui.screenshot()
    captura.save(vn.archivoNombre)

    messagebox.showinfo("Éxito","Captura Guardada")
vn = tk.Tk()
crearWidgets()
mainloop()