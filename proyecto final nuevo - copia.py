import tkinter as tk
from cgitb import text
from select import select
from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql



#------------------------Ventana-de-Inicio----------------------------


def ventana_Login():
			global ventana1
			ventana1 = Tk()
			w = 1650
			h = 850
			ws = ventana1.winfo_screenwidth()
			hs = ventana1.winfo_screenheight()
			x = (ws/2) - (w/2)
			y = (hs/2) - (h/2)
			ventana1.geometry('%dx%d+%d+%d' % (w, h, x, y))
			
			#-----------------------------------------------------------------
			ventana1.title("Iniciar Sesion")
			ventana1.configure(bg="#d6bda5")
		#---------------------------------------------------------
		#-----------------------------------------------------------------
			def login_admin():
				if(usuario1.get() == ""):
					entry_usuario1.focus()
					messagebox.showinfo("Faltan datos", "Ingrese Usuario")

					return
				elif(contrasena1.get()==""):
					messagebox.showinfo("Faltan datos", "Ingrese Contraseña")
					entry_constrasena1.focus()
					return

				basedatos = pymysql.connect(host= "localhost", user="root", passwd="", db="proyectocofee")
				fcursor = basedatos.cursor()

				fcursor.execute("SELECT Usuario FROM admi WHERE Usuario='" + usuario1.get() + "' and Contrasena='" + contrasena1.get() + "'")

				if fcursor.fetchall():
					deRegistro_a_escuela()
				else:
					messagebox.showerror("Error", "Usuario y Contraseña Incorrecta")

				
				basedatos.close()
				
				
#-----------------------------------------------------------------------
			
			# Cargar el logo
			ruta_logo = "logo.png" # Cambia esto por la ruta de tu logo
			logo = Image.open(ruta_logo)
			logo = logo.resize((600, 600))  # Cambia el tamaño si es necesario

			# Convertir el logo para usar con Tkinter
			logo_tk = ImageTk.PhotoImage(logo)

			# Crear un widget de etiqueta para mostrar el logo
			etiqueta_logo = Label(ventana1, image=logo_tk)
			etiqueta_logo.place(x=400, rely=0.5, anchor=CENTER)
			
				



#----------------------------------------------------------------
			Label(ventana1, text="Usuario " ,width=12,font= "Arapey",bg="#d6bda5").place(x=990, y=350)
			Label(ventana1, text="Contraseña",width=12,font= "Arapey",bg="#d6bda5").place(x=990, y=400)
			

			usuario1 = StringVar()
			contrasena1 = StringVar()

			entry_usuario1 = Entry(ventana1, textvariable=usuario1)
			entry_usuario1.pack()
			entry_usuario1.place(x=1100,y=350)

			entry_constrasena1 = Entry(ventana1, textvariable=contrasena1, show="*")
			entry_constrasena1.pack()
			entry_constrasena1.place(x=1100,y=400)
			Button(ventana1, text="Registrarse", command=ventana_Login).place(x=1040, y=500)
			Button(ventana1, text="Entrar").place(x=1150, y=500)
			Button(ventana1, text="SALIR").place(x=1485, y=9)
			
			ventana1.mainloop()


def ventana_registrar_admi():
			
			global ventana2
			ventana2 = Tk()
			w = 1650
			h = 850
			ws = ventana2.winfo_screenwidth()
			hs = ventana2.winfo_screenheight()
			x = (ws/2) - (w/2)
			y = (hs/2) - (h/2)
			ventana2.geometry('%dx%d+%d+%d' % (w, h, x, y))
			
			#-----------------------------------------------------------------
			ventana2.title("Iniciar Sesion")
			ventana2.configure(bg="#d6bda5")


			ventana2.mainloop()



def deRegistro_a_escuela():
	ventana1.destroy()
	ventana_menu
	
ventana_Login()

    
