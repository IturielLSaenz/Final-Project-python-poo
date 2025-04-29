# implementación GUI
from tkinter import *
from tkinter import font
import tkinter as tk
from Person import Person as P
# --- variables necesarias:
global listContactos # Lista vacía que contiene los contactos.
listContactos = []

def allContacts(master):
        new_window = Toplevel(master)
        new_window.geometry("540x700")
        new_window.protocol("WM_DELETE_WINDOW", lambda: None) # Eliminar el boton predeterminado para cerrar.
        new_window.resizable(False, False)
        new_window.title("-- Lista de contactos --")
        custom_font = font.Font(family="Helvetica", size=20)
        new_window.columnconfigure(0,weight=1)
        new_window.columnconfigure(1,weight=1)
        def removeContact():
             # --- Logica para elminar elementos por INDEX ---
             try:
                index = int(indexContact.get())  # Convertir el índice a entero
                del listContactos[index]  # Eliminar el contacto de la lista
                # Limpiar el Listbox
                listaContactos.delete(0, END)
                # Insertar los contactos restantes en el Listbox
                for contact in listContactos:
                     listaContactos.insert(END, contact.toString())
             except (ValueError, IndexError) as e:
                print("Error:", e)  # Puedes manejar el error de manera más elegante, como mostrando un mensaje al usuario.
        def clear():
             # --- Limpiar toda la lista ---
             listaContactos.delete(0,END)
             listContactos.clear()
        # --- Codigo para mostrar texto en la pantalla
        text = Label(new_window, text="-- Sistema Agenda - GUI - 554644 --", anchor="center").grid(columnspan=2, column=0, row=0,sticky="ew",pady=2)
        text = Label(new_window,text="--- Lista de contactos: ---").grid(columnspan=2,column=0,row=3,sticky="ew",pady=5)

        listaContactos = Listbox(new_window,height=24,width=15,bg='grey',activestyle="dotbox",font="Helvetica",fg='white')
        for contact in listContactos:
             listaContactos.insert(END,contact.toString())
        listaContactos.grid(column=0, row=4, columnspan=2, sticky="nsew", padx=10, pady=10)
        text = Label(new_window,text="Borrar por index (0 = inicio)")
        text.grid(column=0,row=5,sticky="ew")
        indexContact = Entry(new_window,font=custom_font)
        indexContact.grid(column=1,row=5,sticky="ew")
        rContact = Button(new_window,text="Eliminar",pady=20,command=removeContact).grid(columnspan=2,column=0,row=6,sticky="ew")
        limpiar = Button(new_window,text="Limpiar",pady=20,command=clear).grid(columnspan=2,column=0,row=7,sticky="ew")
        salir = Button(new_window,text="Salir",command=new_window.destroy,pady=20).grid(column=0,row=8,columnspan=2,sticky="ew")

def openContacts():
    window = Toplevel()
    window.geometry("540x540")
    window.title("GUI - CONTACTOS - 554644")
    window.protocol("WM_DELETE_WINDOW", lambda: None) # Eliminar el boton predeterminado para cerrar.
    window.resizable(False, False)
    custom_font = font.Font(family="Helvetica", size=20)
    window.columnconfigure(0,weight=1)
    window.columnconfigure(1,weight=1)
     # ---- El codigo a continuacion es para crear un contacto: ----
    # Se solicita: Nombre, Telefono, y Correo Electrónico
    # Posteriormente se crea un objeto person para guardar todos los datos.
    def addContact():
        name = nameEntry.get()
        tel = telEntry.get()
        email = emailEntry.get()
        owner = P(name,tel,email)
        listContactos.append(owner)
        nameEntry.delete(0, tk.END)
        telEntry.delete(0, tk.END)
        emailEntry.delete(0, tk.END)
        # print("\n")
        # for i in listContactos:
        #     print(i.toString()) <- solo para debug!
        return listContactos
        
    # --- codigo principal para el aspecto visual ---
    text1 = Label(window, text="-- Sistema Agenda - GUI - 554644 --", anchor="center").grid(columnspan=2, column=0, row=0,sticky="ew",pady=10)
    text2 = Label(window, text="Autor: Ituriel Liebes Saenz \n ID: 554644 \n github: https://github.com/IturielLSaenz", anchor="center").grid(columnspan=2, column=0, row=1,sticky="ew",pady=10)
    text3 = Label(window, text="Sistema de creación de contactos.", anchor="center").grid(columnspan=2, column=0, row=2,sticky="ew")
    text1 = Label(window,text="--- Añade un contacto: ---").grid(columnspan=2,column=0,row=3,sticky="ew",pady=10)
    # Espacio para ingresar el nombre:
    text2 = Label(window,text="Ingresa el nombre: ",pady=10).grid(column=0,row=4,sticky="ew")
    nameEntry = Entry(window,font=custom_font)
    nameEntry.grid(column=1,row=4,sticky="ew")
    # Espacio para ingresar el telefono:
    text3 = Label(window,text="Ingresa el telefono: ",pady=10).grid(column=0,row=5,sticky="ew")
    telEntry = Entry(window,font=custom_font)
    telEntry.grid(column=1,row=5,sticky="ew")
    # Espacio para ingresar el correo electrónico:
    text4 = Label(window,text="Ingresa el email: ",pady=10).grid(column=0,row=6,sticky="ew")
    emailEntry = Entry(window,font=custom_font)
    emailEntry.grid(column=1,row=6,sticky="ew")
    # Botones extra:
    # Un button para continuar hacia el menu de creacion de agenda.
    newContact = Button(window,text="añadir contacto",command=addContact,pady=35).grid(column=0,row=7,sticky="ew")
    seeAll = Button(window,text="Ver contactos",command=lambda: allContacts(window),pady=35).grid(column=1,row=7,sticky="ew")
    done = Button(window,text="Listo",command=window.destroy,pady=35).grid(columnspan=2,column=0,row=8,sticky="ew")
