# Codigo ventana principal y sub procesos de la GUI.
# Autor: Ituriel Liebes Saenz
# ID: 554644
# Tecnologias: Python, Tkinter

# implementación GUI
from tkinter import *
from tkinter import font
import tkinter as tk
from guiFuncs.contacts import openContacts
from guiFuncs.eventos import addEvent
from guiFuncs.global_agenda import newAgenda

window = Tk()
window.protocol("WM_DELETE_WINDOW", lambda: None) # Eliminar el boton predeterminado para cerrar.
window.resizable(False, False)
window.geometry("740x700")
window.title("GUI - Sistema Agenda - 554644")

# --- Funciones necesarias para editar la lista de eventos: ---
def selectEvent(event):
    # Esta funcion recibe el elemento seleccionado o hecho "clic" en la lista 
    # de la agenda, y abre los detalles del evento con dos botones:
    # [Salir] [Eliminar evento] -> ambos botones destruyen la ventana.
    # --- Funcion para abrir una ventana para visualizar el evento seleccionado: ---
    def openSelected():
        window = Toplevel()
        window.geometry("360x360")
        window.title("--- Visualización del evento ---")
        
        pass


    selection_index = listaEventos.curselection()
    if selection_index:
        selected = listaEventos.get(selection_index[0])
        openSelected()
    return selected


    



# --- Codigo principal para el menu ---
# Aqui se muestra todas las opciones principales, cada una se desgloza en una ventana aparte!
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
text1 = Label(window, text="-- Sistema Agenda - GUI - 554644 --", anchor="center").grid(columnspan=2, column=0, row=0,sticky="ew")
text2 = Label(window, text="Autor: Ituriel Liebes Saenz \n ID: 554644 \n github: https://github.com/IturielLSaenz", anchor="center").grid(columnspan=2, column=0, row=1,sticky="ew")
text3 = Label(window, text="Bienvenido a tu agenda!", anchor="center").grid(columnspan=2, column=0, row=2,sticky="ew")

def updateListaEventos():
    listaEventos.delete(0,END)
    for i,evento in enumerate(newAgenda.events): # Usar enumerate para regresar un iterable "numerado"
        listaEventos.insert(END, f"{i + 1}. {evento.previewToString()}")

listaEventos = Listbox(window,height=24,width=15,bg='grey',activestyle="dotbox",font="Helvetica",fg='white')

listaEventos.grid(column=0, row=3, columnspan=2, sticky="nsew", padx=10, pady=10)
listaEventos.bind("<<ListboxSelect>>",selectEvent)
# --- Opciones para el menú principal ---
contactos = Button(window, text="Contactos",pady=30,command=openContacts)
contactos.grid(column=0, row=4,sticky="ew")

eventosBtn = Button(window,text="Añadir Evento",pady=30,command=lambda: addEvent(updateListaEventos))
eventosBtn.grid(column=1,row=4,sticky="ew")

salir = Button(window, text="SALIR", command=window.destroy,pady=30)
salir.grid(columnspan=2,column=0, row=5,sticky="ew")

data = Label(window,text=" 2025 -- tkinter + python",anchor="center").grid(columnspan=2,column=0,row=8,sticky="ew")

# --- funcion para ejecutar la gui ---
def runGui():
    updateListaEventos()
    window.mainloop()