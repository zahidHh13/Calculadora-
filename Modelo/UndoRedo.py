# Laboratorio_07 Implementación de las operaciones "UNDO" Y "REDO" usando Pilas (Stack)

#                   -- UNDO / REDO --

class UndoRedo:
    def __init__(self): #Inicializamos los parámetros para la clase 
        self.Undo = [] #Va a ser un arreglo el undo, creo que pila 
        self.Redo = []#Va a aser otro arreglo el redo, creo que pila 

    def input_char(self, c):
        self.Undo.append(c) #Apend para agregar a la lista un elemento en específico 
        self.Redo.clear()  # Para después de insertar, vaciar la pila Redo. El clear no toma argumetnos, limpia tan solamente toda una lista 
    
    #Modulo del UNDO  
    def undo(self):
        if self.Undo:
            x = self.Undo.pop() #elimina un elemento de la lista en específico y si no tiene nada: pop(), elimina el último elemento de la lista  
            self.Redo.append(x)
            return True
        print("undo: (pila Undo vacía)")
        return False
    
    #Modulo del REDO 
    def redo(self):
        if self.Redo:
            x = self.Redo.pop() 
            self.Undo.append(x)
            return True
        print("redo: (pila Redo vacía)")
        return False

    def show(self):
        if self.Undo: 
            return self.Undo[-1].copy()
        return 

    def simulate(self, ops):
        for op in ops:
            if op == "UNDO":
                if self.undo():
                    print(f"undo: {self.show()}")
            elif op == "REDO":
                if self.redo():
                    print(f"redo: {self.show()}")
            else:
                self.input_char(op.strip()) #para que es el strip 
                print(f"inserta: {self.show()}")

# Prueba de la clase UndoRedo


if __name__ == "__main__":
    ops = ["12", "-", "8", "UNDO", "REDO"]
    ur = UndoRedo()
    ur.simulate(ops) #llamamos al modulo simulate 

