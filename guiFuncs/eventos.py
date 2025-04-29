# implementación GUI
from tkinter import *
from tkinter import font
from tkinter import ttk
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
    window.geometry("540x340")
    window.title("GUI - Sistema Agenda - 554644")

    # --- Codigo principal para el menu ---
    # Aqui se muestra todas las opciones principales, cada una se desgloza en una ventana aparte!
    window.columnconfigure(0,weight=1)
    window.columnconfigure(1,weight=1)


    # ---- Display ----
    text = Label(window, text="-- Sistema Agenda - GUI - 554644 --", anchor="center").grid(columnspan=2, column=0, row=0,sticky="ew",pady=2)
    text = Label(window,text="--- Lista de eventos (AGENDA): ---").grid(columnspan=2,column=0,row=1,sticky="ew",pady=10)
    newEvent = Button(window, text="Añadir evento",pady=60,command=addEvent)
    newEvent.grid(column=0, row=2,sticky="ew")
    notEvent = Button(window, text="Remover evento",pady=60)
    notEvent.grid(column=1, row=2,sticky="ew")

    salir = Button(window, text="Salir",pady=40,command=window.destroy)
    salir.grid(columnspan=2,column=0, row=3,sticky="ew")

def addEvent():
    window = Toplevel()
    #window.protocol("WM_DELETE_WINDOW", lambda: None) # Eliminar el boton predeterminado para cerrar.
    #window.resizable(False, False)
    window.geometry("740x540")
    window.title("GUI - Sistema Agenda - 554644")
    window.columnconfigure(0,weight=1)
    window.columnconfigure(1,weight=1)
    window.columnconfigure(2,weight=1)
    window.columnconfigure(3,weight=1)

    # --- Display ----
    text = Label(window, text="-- Sistema Agenda - GUI - 554644 --", anchor="center").grid(columnspan=4, column=0, row=0,sticky="ew",pady=2)
    text = Label(window,text=" Añade un evento nuevo:").grid(columnspan=4,column=0,row=1,sticky="ew")
    # --- formulario para rellenar y obtener un evento nuevo en la lista de eventos ---
    # --- Ingresar contacto ---
    text = Label(window,text="Contacto: ").grid(columnspan=1,column=0,row=2,sticky="ew")
    contactoEntry = Entry(window,width=10)
    # contactoEntry.config(state="disabled")
    contactoEntry.grid(columnspan=2,column=1,row=2,sticky="ew")
    contactoBtn = Button(window,text="Buscar").grid(columnspan=1,column=3,row=2,sticky="ew")
    # --- Ingresar asunto ---
    text = Label(window,text="Asunto: ").grid(columnspan=1,column=0,row=3,sticky="ew")
    asuntoEntry = Entry(window,width=10)
    asuntoEntry.grid(columnspan=3,column=2,row=3,sticky="ew")
    # --- Ingresar fecha ---
    # fecha: [entry] [entry] [entry]
    text = Label(window,text="Fecha: ").grid(columnspan=1,column=0,row=4,sticky="ew")
    diaEntry = Entry(window,width=10)
    diaEntry.grid(columnspan=1,column=1,row=4,sticky="ew")
    mesEntry = Entry(window,width=10)
    mesEntry.grid(columnspan=1,column=2,row=4,sticky="ew")
    annEntry = Entry(window,width=10)
    annEntry.grid(columnspan=1,column=3,row=4,sticky="ew")
    # --- Ingresar horaInicio ---
    # Hora: [entry] [entry] [entry]
    text = Label(window,text="Hora Inicio: ").grid(columnspan=1,column=0,row=5,sticky="ew")
    horaInEntry = Entry(window,width=10)
    horaInEntry.grid(columnspan=1,column=1,row=5,sticky="ew")
    minInEntry = Entry(window,width=10)
    minInEntry.grid(columnspan=1,column=2,row=5,sticky="ew")
    secInEntry = Entry(window,width=10)
    secInEntry.grid(columnspan=1,column=3,row=5,sticky="ew")
    # --- Ingresar horaFin ---
    # Hora: [entry] [entry] [entry]
    text = Label(window,text="Hora Inicio: ").grid(columnspan=1,column=0,row=6,sticky="ew")
    horaFnEntry = Entry(window,width=10)
    horaFnEntry.grid(columnspan=1,column=1,row=6,sticky="ew")
    minFnEntry = Entry(window,width=10)
    minFnEntry.grid(columnspan=1,column=2,row=6,sticky="ew")
    secFnEntry = Entry(window,width=10)
    secFnEntry.grid(columnspan=1,column=3,row=6,sticky="ew")
    # --- Ingresar descripción del evento ---
    text = Label(window,text="Descripción: ").grid(columnspan=1,column=0,row=7,sticky="ew")
    descEntry = Entry(window)
    descEntry.grid(columnspan=3,column=1,row=7,sticky="ew")
    # --- botón para terminar ---
    submit = Button(window,text="Enviar",pady=30).grid(columnspan=2,column=1,row=8,sticky="ew")