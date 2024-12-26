# Modelo/calculador_modelo.py

import re
from .stack import Stack
import math

class CalculadorModelo:
    def __init__(self):
        self.entrada = ""
        self.historial = []  # Para UNDO 
        self.redo_stack = []  # Para REDO 

    def agregar_a_entrada(self, valor):
        self.historial.append(self.entrada)  # Guardar el estado actual para undo
        self.redo_stack.clear()  # Limpiar el redo stack al agregar algo nuevo
        self.entrada += str(valor)

    def limpiar_entrada(self):
        self.entrada = ""

    def obtener_entrada(self):
        return self.entrada

    def calcular(self, expresion):
        if not self.validar_parentesis(expresion):
            return "Error: Paréntesis desbalanceados"
        
        postfija = self.convertir_a_postfijo(expresion)
        resultado = self.evaluar_postfijo(postfija)
        return resultado

    def validar_parentesis(self, expresion):
        stack = []
        pares = {')': '(', ']': '[', '}': '{'}

        for char in expresion:
            if char in pares.values():
                stack.append(char)
            elif char in pares.keys():
                if stack == [] or pares[char] != stack.pop():
                    return False
        
        return stack == []  # Verifica si el stack está vacío al final

    def convertir_a_postfijo(self, expresion):
        stack = []
        salida = []
        tokens = self.tokenizar(expresion)

        for token in tokens:
            if self.es_numero(token):
                salida.append(token)
            elif token == 'sqrt':  # Agregar sqrt directamente a la salida
                salida.append(token)
            elif token in '+-*/^':
                while stack and self.precedencia(stack[-1]) >= self.precedencia(token):
                    salida.append(stack.pop())
                stack.append(token)
            elif token in '([{':
                stack.append(token)
            elif token in ')]}':
                while stack and stack[-1] not in '([{':
                    salida.append(stack.pop())
                stack.pop()  # Sacar el paréntesis correspondiente

        while stack:
            salida.append(stack.pop())
        return salida

    #Convertir una expresion matemática en una lista de tokens 
    def tokenizar(self, expresion):
        tokens = []
        numero_actual = ''
        funciones = ['sqrt']  # Agregar reconocimiento de funciones

        i = 0
        while i < len(expresion):
            char = expresion[i]
            if char.isdigit() or char == '.':
                numero_actual += char  # Agrega el número o punto decimal
            else:
                if numero_actual:
                    tokens.append(numero_actual)  # Añadir el número completo
                    numero_actual = ''
                if expresion[i:i+4] in funciones:  # Verificar si es una función reconocida
                    tokens.append(expresion[i:i+4])
                    i += 3  # Saltar los siguientes caracteres de 'sqrt'
                elif char in '+-*/^()[]{}':
                    tokens.append(char)
            i += 1
            
        if numero_actual:  # Añadir el último número si existe
            tokens.append(numero_actual)

        return tokens


    def es_numero(self, token):
        try:
            float(token)  # Intentar convertir a float para verificar si es un número
            return True
        except ValueError:
            return False

    def precedencia(self, operador):
        if operador in '+-':
            return 1
        elif operador in '*/':
            return 2
        elif operador == '^':
            return 3
        return 0

    def evaluar_postfijo(self, postfija):
        stack = []
        
        for token in postfija:
            if self.es_numero(token):
                stack.append(float(token))  # Asegurarse de que se manejen como float
            elif token in '+-*/^':
                b = stack.pop()
                a = stack.pop()
                resultado = self.calcular_operacion(a, b, token)
                if isinstance(resultado, str):  # Verificar si hubo un error
                    return resultado
                stack.append(resultado)
            elif token == 'sqrt':
                a = stack.pop()
                if a < 0:
                    return "Error: Raíz cuadrada de número negativo"  # Verificar que no se intente raíz negativa
                resultado = math.sqrt(a)
                stack.append(resultado)

        return stack[0] if stack else 0


    def calcular_operacion(self, a, b, operador):
        if operador == '+':
            return a + b
        elif operador == '-':
            return a - b
        elif operador == '*':
            return a * b
        elif operador == '/':
            if b == 0:  # Verificar si se intenta dividir entre cero
                return "Error: División por cero"
            return a / b
        elif operador == '^':
            return a ** b

    def deshacer(self):
        if self.historial:
            self.redo_stack.append(self.entrada)  # Agregar a redo
            self.entrada = self.historial.pop()  # Recuperar el último estado

    def rehacer(self):
        if self.redo_stack:
            self.historial.append(self.entrada)  # Guardar el estado actual para undo
            self.entrada = self.redo_stack.pop()  # Recuperar el último estado
