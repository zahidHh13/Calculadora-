from stack import Stack 


def is_correct_parenthesis(expression):
    pila = Stack()
    simbolos = {')': '(', ']': '[', '}': '{'}
    for c in expression:
        if c in simbolos.values():  
            pila.push(c)
        elif c in simbolos:  
            if pila.is_empty() or pila.pop() != simbolos[c]:
                return False
    return pila.is_empty()
