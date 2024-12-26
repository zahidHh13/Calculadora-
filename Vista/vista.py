# Vista/vista.py

from customtkinter import *
from tkinter import messagebox

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = CTk()
        self.root.title("MiCalculadora")
        self.root.geometry("360x490")
        self.root.iconbitmap("Iconos/IconoMiCalculadora.ico")
        set_appearance_mode("dark")  # Establecer modo oscuro
        set_default_color_theme("dark-blue")  # Color azul por defecto

        # Entrada para mostrar la expresión actual
        self.entrada = CTkEntry(self.root, width=300, height=40, font=("Arial", 20))
        self.entrada.grid(row=0, column=1, columnspan=4, padx=10, pady=10)

        # Nueva barra de salida para mostrar resultados
        self.resultado = CTkEntry(self.root, width=300, height=40, font=("Arial", 20), state='readonly')  # Solo lectura
        self.resultado.grid(row=1, column=1, columnspan=4, padx=10, pady=10)

        self.crear_botones()
        self.root.mainloop()

    def crear_botones(self):
        # Matriz de botones que incluye todos los números y operaciones
        botones = [
            ('7', 2, 1), ('8', 2, 2), ('9', 2, 3), ('+', 2, 4),
            ('4', 3, 1), ('5', 3, 2), ('6', 3, 3), ('-', 3, 4),
            ('1', 4, 1), ('2', 4, 2), ('3', 4, 3), ('*', 4, 4),
            ('0', 5, 1), ('.', 5, 2), ('=', 5, 3), ('/', 5, 4),
            ('(', 6, 1), (')', 6, 2), ('sqrt', 6, 3), ('^', 6, 4),
            ('⬅️', 7, 1), ('➡️', 7, 2), ('C', 7, 3), ('⌫', 7, 4)
        ]

        # Crear botones
        for (texto, fila, col) in botones:
            if texto in '0123456789':  # Botones de números
                self.crear_boton(texto, fila, col, fg_color="#691d37")  # Color para los números
            elif texto == '=':  # Botón '='
                self.crear_boton(texto, fila, col, fg_color="#073b3f")  # Color para el '='
            else:
                self.crear_boton(texto, fila, col)  # Botones estándar

    def crear_boton(self, texto, fila, col, fg_color="default"):
        # Crear botón con customtkinter
        if fg_color == "default":
            boton = CTkButton(self.root, text=texto, width=80, height=50, command=lambda: self.pulsar_boton(texto))
        else:
            boton = CTkButton(self.root, text=texto, width=80, height=50, fg_color=fg_color, command=lambda: self.pulsar_boton(texto))
        
        boton.grid(row=fila, column=col, padx=5, pady=5)

    def pulsar_boton(self, texto):
        if texto == '=':
            expresion = self.controlador.modelo.obtener_entrada()
            resultado = self.controlador.modelo.calcular(expresion)
            if isinstance(resultado, str) and resultado.startswith("Error"):
                messagebox.showerror("Error", resultado)  # Mostrar mensaje de error
            else:
                self.mostrar_resultado(resultado)  # Mostrar resultado en la barra de salida
        elif texto == 'C':
            self.controlador.modelo.limpiar_entrada()
            self.entrada.delete(0, 'end')
            self.resultado.delete(0, 'end')  # Limpiar la barra de resultados
        elif texto == '⌫':
            self.borrar_entrada()
        elif texto == '⬅️':
            self.controlador.modelo.deshacer()
            self.actualizar_entrada()
        elif texto == '➡️':
            self.controlador.modelo.rehacer()
            self.actualizar_entrada()
        else:
            self.controlador.modelo.agregar_a_entrada(texto)
            self.entrada.insert('end', texto)  # Insertar directamente sin espacios

    def mostrar_resultado(self, resultado):
        self.resultado.configure(state='normal')  # Permitir edición temporal
        self.resultado.delete(0, 'end')  # Limpiar la barra de resultados
        self.resultado.insert(0, resultado)  # Insertar resultado
        self.resultado.configure(state='readonly')  # Volver a modo solo lectura

    def borrar_entrada(self):
        current_text = self.entrada.get()
        if current_text:  # Asegurarse de que haya algo que borrar
            self.entrada.delete(len(current_text) - 1, 'end')

    def actualizar_entrada(self):
        self.entrada.delete(0, 'end')  # Limpiar entrada
        self.entrada.insert(0, self.controlador.modelo.obtener_entrada())  # Actualizar con el nuevo valor
