# implementación GUI
from tkinter import *
from tkinter import font
import tkinter as tk

# --- objetos ---
from Date import Date as D
from Time import Time as T
from Event import Event as E
from Agenda import Agenda as A

def openEventos():
    window = Toplevel()
    window.protocol("WM_DELETE_WINDOW", lambda: None) # Eliminar el boton predeterminado para cerrar.
    window.resizable(False, False)
    window.geometry("540x540")
    window.title("GUI - Sistema Agenda - 554644")

    # --- Codigo principal para el menu ---
    # Aqui se muestra todas las opciones principales, cada una se desgloza en una ventana aparte!
    window.columnconfigure(0,weight=1)
    window.columnconfigure(1,weight=1)


    # ---- Display ----
    text = Label(window, text="-- Sistema Agenda - GUI - 554644 --", anchor="center").grid(columnspan=2, column=0, row=0,sticky="ew",pady=2)
    text = Label(window,text="--- Lista de eventos (AGENDA): ---").grid(columnspan=2,column=0,row=3,sticky="ew",pady=5)
    newEvent = Button(window, text="Añadir evento",pady=20)
    newEvent.grid(column=0, row=5,sticky="ew")
    notEvent = Button(window, text="Remover evento",pady=20)
    notEvent.grid(column=1, row=5,sticky="ew")

    showEvent = Button(window, text="Mostrar eventos",pady=20)
    showEvent.grid(column=0, row=6,sticky="ew")
    listEvents = Button(window, text="Lista de eventos",pady=20)
    listEvents.grid(column=1, row=6,sticky="ew")

    getEventIndex = Button(window, text="Buscar evento",pady=20)
    getEventIndex.grid(column=0, row=7,sticky="ew")