from model.stack import Stack
# Clase para evaluar la expresión postfija

"""
Utilizamos una pila para realizar las operaciones en el orden correcto. 
A medida que se encuentran operadores, se extraen los operandos dela pila, se ejecuta la 
operación y el resultado se empuja nuevamente a la pila. Al finalizar, la pila 
contiene el resultado final de la expresión
"""
class EvalPost: 
    def __init__(self):
        self.stack = Stack()

    # Función para evaluar la expresión postfija
    def evalPostfija(self, expression): 
        expression = expression.strip()
        
        postfijo = expression.split()  
        
        for s in postfijo:
            if s == "+":
                opnd2 = self.stack.pop()
                opnd1 = self.stack.pop()
                self.stack.push(opnd1 + opnd2)
            
            elif s == "-":
                opnd2 = self.stack.pop()
                opnd1 = self.stack.pop()
                self.stack.push(opnd1 - opnd2)
            
            elif s == "*":
                opnd2 = self.stack.pop()
                opnd1 = self.stack.pop()
                self.stack.push(opnd1 * opnd2)
            
            elif s == "/":
                opnd2 = self.stack.pop()
                opnd1 = self.stack.pop()
                self.stack.push(opnd1 / opnd2)
            
            elif s == "**":
                opnd2 = self.stack.pop()
                opnd1 = self.stack.pop()
                self.stack.push(opnd1 ** opnd2)

            elif s == "sqrt":
                opnd1 = self.stack.pop()
                self.stack.push(opnd1 ** 0.5)

            else:
                self.stack.push(float(s))  
        
        return self.stack.peek()
    
