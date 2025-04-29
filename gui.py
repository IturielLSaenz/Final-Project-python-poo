# Codigo Backend para toda la GUI y procesos: 
# Autor: Ituriel Liebes Saenz
# ID: 554644
# Tecnologias: Python, Tkinter

# implementación GUI
from tkinter import *
from tkinter import font
import tkinter as tk
from guiFuncs.contacts import openContacts
from guiFuncs.eventos import openEventos

window = Tk()
window.protocol("WM_DELETE_WINDOW", lambda: None) # Eliminar el boton predeterminado para cerrar.
window.resizable(False, False)
window.geometry("540x540")
window.title("GUI - Sistema Agenda - 554644")

# --- Codigo principal para el menu ---
# Aqui se muestra todas las opciones principales, cada una se desgloza en una ventana aparte!
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
text1 = Label(window, text="-- Sistema Agenda - GUI - 554644 --", anchor="center").grid(columnspan=2, column=0, row=0,sticky="ew")
text2 = Label(window, text="Autor: Ituriel Liebes Saenz \n ID: 554644 \n github: https://github.com/IturielLSaenz", anchor="center").grid(columnspan=2, column=0, row=1,sticky="ew")
text3 = Label(window, text="Bienvenido al sistema de creación de agenda.", anchor="center").grid(columnspan=2, column=0, row=2,sticky="ew")

menuHeader = Label(window, text=" -- OPCIONES --", anchor="center").grid(columnspan=2, column=0, row=3, pady=2,sticky="ew")
# --- Opciones para el menú principal ---
contactos = Button(window, text="Contactos",pady=40,command=openContacts)
contactos.grid(columnspan=2, column=0, row=4,sticky="ew")

eventosBtn = Button(window,text="Eventos",pady=40,command=openEventos)
eventosBtn.grid(columnspan=2,column=0,row=5,sticky="ew")


salir = Button(window, text="SALIR", command=window.destroy,pady=40)
salir.grid(columnspan=2,column=0, row=7,sticky="ew")

data = Label(window,text=" 2025 -- tkinter + python",anchor="center").grid(columnspan=2,column=0,row=8,sticky="ew",pady=30)

# --- funcion para ejecutar la gui ---
def runGui():
    window.mainloop()