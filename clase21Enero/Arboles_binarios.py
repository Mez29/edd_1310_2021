#Clase 21/01/2021

class NodoArbol:
    def __init__(self, value, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def insert(self, value):
        if self.__root == None:
            self.__root = NodoArbol(value, None, None)
        else:
            self.__insert__(self.__root, value)

    def __insert__(self, nodo, value):
        if nodo.data == value:
            print("El dato ya existe, no se ingresa nada")
        elif value < nodo.data:
            if nodo.left == None:
                nodo.left == NodoArbol(value)
            else:
                self.__insert__(nodo.left, value)
        else:
            if nodo.right == None:
                nodo.right = NodoArbol(value)
            else:
                self.__insert__(nodo.right, value)

    def __recorrido_in(self, nodo):
        if nodo != None:
            self.__recorrido_in(nodo.left)
            print(nodo.data, end= ", ")
            self.__recorrido_in(nodo.right)

    def __recorrido_pos( self , nodo ):
        if nodo:
            self.__recorrido_pos(nodo.left)
            self.__recorrido_pos(nodo.right)
            print(nodo.data, end=",")

    def __recorrido_pre(self , nodo):
        if nodo:
            print(nodo.data , end=",")
            self.__recorrido_pre(nodo.left)
            self.__recorrido_pre(nodo.right)


    def transversal(self, format = "inorden"):
        if format == "inorden":
            self.__recorrido_in(self.__root)
        elif format == 'preorden':
            print('Recorrido en preorden...')
            self.__recorrido_pre(self.__root)
        elif format == 'posorden':
            print('Recorrido en posorden')
            self.__recorrido_pos(self.__root)
        else:
            print("Error, ese formato no existe")
        print("")


    def search(self , value ):
        if self.__root == None:
            print("Vacio")
            return None
        else:
            return self.__search( self.__root , value)

    def __search( self , nodo , value ):
        if nodo == None: # esta vacio?
            print("Caso base")
            return None
        elif nodo.data == value: # caso base de recursividad
            print("ENCONTRADO")
            return nodo #tambien se puede regresar solo True /False
        elif value < nodo.data:
            print("Busca a la izquierda")
            return self.__search( nodo.left , value)
        else:
            print("Buscar a la izquierda")
            return self.__search( nodo.right , value)

    def remove( self , value ):
        encontrado = self.search(value)
        # caso 1
        if encontrado.left == None and encontrado.right == None:
            print("Eliminando", encontrado.data)
            encontrado = None
        #caso 2
        elif (encontrado.left != None and encontrado.right == None) or \
        (encontrado.left == None and encontrado.right != None):
            print("A eliminar:", encontrado.data)
            
