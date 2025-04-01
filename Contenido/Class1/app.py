# from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random


class App:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        # self.imagenesg = ["C:/Users/Usuario/Documents/Programacion-DavidLlerena/M5/M5/Contenido/Class1/Img/1.png",
        #                 "C:/Users/Usuario/Documents/Programacion-DavidLlerena/M5/M5/Contenido/Class1/Img/2.png",
        #                 "C:/Users/Usuario/Documents/Programacion-DavidLlerena/M5/M5/Contenido/Class1/Img/3.png",
        #                 "C:/Users/Usuario/Documents/Programacion-DavidLlerena/M5/M5/Contenido/Class1/Img/4.png",
        #                 "C:/Users/Usuario/Documents/Programacion-DavidLlerena/M5/M5/Contenido/Class1/Img/5.png"]
        self.imagenesb = ["C:/Users/Usuario/Documents/Programacion-DavidLlerena/M5/M5/Contenido/Class1/Imgb/1.png",
                          "C:/Users/Usuario/Documents/Programacion-DavidLlerena/M5/M5/Contenido/Class1/Imgb/2.png",
                          "C:/Users/Usuario/Documents/Programacion-DavidLlerena/M5/M5/Contenido/Class1/Imgb/3.png",
                          "C:/Users/Usuario/Documents/Programacion-DavidLlerena/M5/M5/Contenido/Class1/Imgb/4.png",
                          "C:/Users/Usuario/Documents/Programacion-DavidLlerena/M5/M5/Contenido/Class1/Imgb/5.png"]

        root.title("Ingresar Datos")

        self.setup_ui()


    def setup_ui(self):

        # ttk.Label(self.root, text="Marca").grid(column=0, row=0)  # Cambiado a ttk.Label
        # self.marca = tk.StringVar()
        # ttk.Entry(self.root, textvariable=self.marca).grid(column=1, row=0)

        # ttk.Label(self.root, text="Procesador").grid(column=0, row=1)  # Cambiado a ttk.Label
        # self.procesador = tk.StringVar()
        # ttk.Entry(self.root, textvariable=self.procesador).grid(column=1, row=1)
       
        # ttk.Label(self.root, text="Memoria").grid(column=0, row=2)  # Cambiado a ttk.Label
        # self.memoria = tk.StringVar()
        # ttk.Entry(self.root, textvariable=self.memoria).grid(column=1, row=2)

        # ttk.Label(self.root, text="Tarjeta Grafica").grid(column=0, row=3)  # Cambiado a ttk.Label
        # self.tarjeta = tk.StringVar()
        # ttk.Entry(self.root, textvariable=self.tarjeta).grid(column=1, row=3)

        # ttk.Label(self.root, text="Precio").grid(column=0, row=4)  # Cambiado a ttk.Label
        # self.precio = tk.StringVar()
        # ttk.Entry(self.root, textvariable=self.precio).grid(column=1, row=4)

        # ttk.Button(self.root, text="Agregar Laptop", command=self.agregar_laptop).grid(column=0, row=5, columnspan=2)

        # self.mostrar_laptop = tk.Text(self.root, width=50, height=10)
        # self.mostrar_laptop.grid(column=0, row=6, columnspan=2) 

        # self.canva = tk.Canvas(self.root, width=200, height=200)
        # self.canva.grid(column=3, row=1, rowspan = 5)

        ttk.Label(self.root, text="Marca").grid(column=0, row=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(column=1, row=0)

        ttk.Label(self.root, text="Procesador").grid(column=0, row=1)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(column=1, row=1)

        ttk.Label(self.root, text="Memoria").grid(column=0, row=2)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(column=1, row=2)

        ttk.Label(self.root, text="Almacenamiento").grid(column=0, row=3)
        self.almacenamiento = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.almacenamiento).grid(column=1, row=3)

        ttk.Label(self.root, text="Precio").grid(column=0, row=4)
        self.precio = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.precio).grid(column=1, row=4)

        ttk.Label(self.root, text="Duración Batería").grid(column=0, row=5)
        self.duracion_bateria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.duracion_bateria).grid(column=1, row=5)

        ttk.Button(self.root, text="Agregar Laptop", command=self.agregar_laptop).grid(column=0, row=6, columnspan=2)

        self.mostrar_laptop = tk.Text(self.root, width=50, height=10)
        self.mostrar_laptop.grid(column=0, row=7, columnspan=2)

        self.canva = tk.Canvas(self.root, width=200, height=200)
        self.canva.grid(column=3, row=1, rowspan=5)



    def agregar_laptop(self):
        # nueva_laptop = Laptop_Gaming(self.marca.get(), self.procesador.get(), self.memoria.get(), self.tarjeta.get(), self.precio.get())
        # self.laptops.append(nueva_laptop)

        # Validar que todos los campos estén completos
        if not all([self.marca.get(), self.procesador.get(), self.memoria.get(),
                    self.almacenamiento.get(), self.precio.get(), self.duracion_bateria.get()]):
            print("Por favor, completa todos los campos.")
            return

        # Crear una nueva instancia de Laptop_Business
        nueva_laptop = Laptop_Business(
            self.marca.get(),               # Marca
            self.procesador.get(),          # Procesador
            self.memoria.get(),             # RAM
            float(self.precio.get()),       # Precio
            0,                              # Descuento (valor predeterminado)
            self.almacenamiento.get(),      # Almacenamiento
            self.duracion_bateria.get()     # Duración de la batería
        )

        # Agregar la laptop a la lista
        self.laptops.append(nueva_laptop)

        # Mostrar la información de la laptop en el cuadro de texto
        self.mostrar_laptop.insert(tk.END, f"{nueva_laptop}\n")

        # Mostrar una imagen aleatoria de las imágenes empresariales
        self.mostrar_imagen_aleatorias()
        pass

    def mostrar_imagen_aleatorias(self):
        imagen_path = random.choice(self.imagenesb)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)
        self.canva.create_image(0, 0, anchor=tk.NW ,image=photo) 
        self.canva.image = photo
        pass


root = tk.Tk()

app = App(root)
root.mainloop()