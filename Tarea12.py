class NodoArbol:
    def __init__(self, value, left = None, right= None):
        self.data = value
        self.left = left
        self.right = right

print("\n")
print("    DEFINICION   ")
print("\n")
print("-------------------------------------------------------------------------")
print("  PREFIJO:")
print("  Indica que el operador va antes de los operandos sus caracteristicas")
print("-------------------------------------------------------------------------")
print("  POSFIJO:")
print("  El operador ocupa la posicion despues de los operandos")
print("-------------------------------------------------------------------------")
print("  INFIJO:")
print("  El operador esta entre los operandos")
print("-------------------------------------------------------------------------")

def main_1():
    print("\n")
    print("          ARBOL 1")
    print("\n")
    arbol_1 = NodoArbol('(+)', NodoArbol('(-)', NodoArbol(6), NodoArbol(5)) , NodoArbol('(*)', NodoArbol(4), NodoArbol(3)))
    print(f"            {arbol_1.data}")
    print("           |   |")
    print(f"       {arbol_1.left.data}       {arbol_1.right.data}")
    print("      |   |     |   |")
    print(f"     {arbol_1.left.left.data}     {arbol_1.left.right.data}   {arbol_1.right.left.data}     {arbol_1.right.right.data}  ")
    print("\n-----------------------------------------------")
    print(f"Orden Prefijo: {arbol_1.data}   {arbol_1.left.data}   {arbol_1.left.left.data}   {arbol_1.left.right.data}   {arbol_1.right.data}   {arbol_1.right.left.data}   {arbol_1.right.right.data}")
    print("-----------------------------------------------")
    print(f" Orden Posfijo: {arbol_1.left.left.data}   {arbol_1.left.right.data}   {arbol_1.left.data}  {arbol_1.right.left.data}    {arbol_1.right.right.data}   {arbol_1.right.data}   {arbol_1.data}")
    print("-----------------------------------------------")
    print(f" Orden Infijo: {arbol_1.left.left.data}   {arbol_1.left.data}   {arbol_1.left.right.data}   {arbol_1.data}   {arbol_1.right.left.data}   {arbol_1.right.data}   {arbol_1.right.right.data} ")
    print("-----------------------------------------------")
    print("\n")
main_1()

def main_2():
    print("\n\n          ARBOL 2")
    print("\n")
    arbol_2 = NodoArbol(50, NodoArbol(40 , NodoArbol(55) , NodoArbol(45)) , NodoArbol(60 , NodoArbol(55) , NodoArbol(70)) )
    print(f"            {arbol_2.data}")
    print("           |  |")
    print(f"        {arbol_2.left.data}      {arbol_2.right.data}")
    print("      |    |  |    |")
    print(f"    {arbol_2.left.left.data}    {arbol_2.left.right.data}  {arbol_2.right.left.data}     {arbol_2.right.right.data}  ")
    print("\n")
    print("-----------------------------------------------")
    print(f" Orden Prefijo: {arbol_2.data}   {arbol_2.left.data}   {arbol_2.left.left.data}   {arbol_2.left.right.data}   {arbol_2.right.data}   {arbol_2.right.left.data}   {arbol_2.right.right.data}")
    print("-----------------------------------------------")
    print(f" Orden Posfijo: {arbol_2.left.left.data}   {arbol_2.left.right.data}   {arbol_2.left.data}   {arbol_2.right.left.data}   {arbol_2.right.right.data}   {arbol_2.right.data}   {arbol_2.data}")
    print("-----------------------------------------------")
    print(f" Orden Infijo: {arbol_2.left.left.data}   {arbol_2.left.data}   {arbol_2.left.right.data}   {arbol_2.data}   {arbol_2.right.left.data}   {arbol_2.right.data}   {arbol_2.right.right.data}")
    print("-----------------------------------------------")
main_2()
