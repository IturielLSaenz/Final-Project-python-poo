# implementación GUI
from tkinter import *
from tkinter import font
from tkinter import ttk
import tkinter as tk

# --- objetos ---
from Date import Date as D
from Time import Time as T
from Event import Event as E
from guiFuncs.contacts import listContactos
from guiFuncs.global_agenda import newAgenda

finalContact = [None] # lista de un solo elemento para guardar la selección

# --- función para abrir una ventana que permite seleccionar un evento y eliminarlo
def removeEvent():
    window = Toplevel()
    window.protocol("WM_DELETE_WINDOW",lambda:None)
    window.resizable(False,False)
    window.geometry("740x540")
    window.title("Eliminar evento")

    done = Button(window,text="Select",command=window.destroy).grid(column=0,row=0,sticky="ew")
# --- función para abrir ventana que permite añadir un nuevo evento
def addEvent(refreshCallback):
    window = Toplevel()
    window.protocol("WM_DELETE_WINDOW", lambda: None) # Eliminar el boton predeterminado para cerrar.
    window.resizable(False, False)
    window.geometry("740x340")
    window.title("Agregar evento")
    window.columnconfigure(0,weight=1)
    window.columnconfigure(1,weight=1)
    window.columnconfigure(2,weight=1)
    window.columnconfigure(3,weight=1)

    # --- special funcs ---
    def searchContact():
        new_window = Toplevel()
        new_window.geometry("400x500")
        new_window.title("Buscar contacto")
        new_window.columnconfigure(0,weight=1)
        new_window.columnconfigure(1,weight=1)

        def onClick(event):
            selected_indices = contact_container.curselection() # los indices seleccionados están en la lista
            if selected_indices:
                selected = contact_container.get(selected_indices[0])
                finalContact[0] = selected
                print(f"Elemento seleccionado: {selected}")
        def storeSelected():
            if finalContact[0] is not None:
                contactoEntry.config(state="normal")
                contactoEntry.delete(0, END)
                contactoEntry.insert(END,str(finalContact[0]))
                contactoEntry.config(state="readonly")
            new_window.destroy()
        text = Label(new_window,text="Lista de contactos:").grid(columnspan=2,column=0,row=0,sticky="ew")
        contact_container = Listbox(new_window,height=24,width=15,bg='grey',activestyle="dotbox",font="Helvetica",fg='white')
        for contact in listContactos:
            contact_container.insert(END,contact.toString())
        contact_container.grid(column=0, row=1, columnspan=2, sticky="nsew", padx=10, pady=10)
        contact_container.bind("<<ListboxSelect>>",onClick)
        select = Button(new_window,text="Select",command=storeSelected).grid(columnspan=2,column=0,row=2)
        return finalContact
    
    # --- submit sirve para crear el evento y terminar el proceso de esta ventana ---
    def onSubmit():
        try:
            # --- declarar variables para crear los respectivos objetos ---
            subject = asuntoEntry.get() # Asunto para el evento
            desc = descEntry.get() # Descripcion del evento
            person = finalContact[0] # Persona del evento
            fecha = D(int(annEntry.get()),int(mesEntry.get()),int(diaEntry.get())) # Crea la fecha para el evento
            horaInicio = T(int(horaInEntry.get()),int(minInEntry.get()),int(secInEntry.get())) # Crea la hora de inicio
            horaFin = T(int(horaFnEntry.get()),int(minFnEntry.get()),int(secFnEntry.get())) # Crea la hora de fin
            # --- creando el evento ---
            evento = E(subject,desc,person,fecha,horaInicio,horaFin)
            print(evento.toString()) # <-- solo para hacer debug!
            newAgenda.addEvent(evento)
            refreshCallback()  # Actualiza la lista en la ventana principal
            window.destroy()
        except Exception:
            window.destroy()
            raise Exception
    # --- Display ----
    text = Label(window, text="-- Sistema Agenda - GUI - 554644 --", anchor="center").grid(columnspan=4, column=0, row=0,sticky="ew",pady=2)
    text = Label(window,text=" Añade un evento nuevo:").grid(columnspan=4,column=0,row=1,sticky="ew")
    # --- formulario para rellenar y obtener un evento nuevo en la lista de eventos ---
    # --- Ingresar contacto ---
    text = Label(window,text="Contacto: ").grid(columnspan=1,column=0,row=2,sticky="ew")
    contactoEntry = Entry(window,width=10,state="readonly")
    # contactoEntry.config(state="disabled")
    contactoEntry.grid(columnspan=2,column=1,row=2,sticky="ew")
    contactoBtn = Button(window,text="Buscar",command=searchContact).grid(columnspan=1,column=3,row=2,sticky="ew")
    # --- Ingresar asunto ---
    text = Label(window,text="Asunto: ").grid(columnspan=1,column=0,row=3,sticky="ew")
    asuntoEntry = Entry(window,width=10)
    asuntoEntry.grid(columnspan=3,column=1,row=3,sticky="ew")
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
    submit = Button(window,text="Enviar",pady=30,command=onSubmit).grid(columnspan=2,column=0,row=8,sticky="ew")
    salir = Button(window,text="SALIR",pady=30,command=window.destroy).grid(columnspan=2,column=2,row=8,sticky="ew")