class Single_Linked_List:
    class _Nodo:
        def __init__(self,valor):
               self.valor = valor
               self.nodo_siguiente = None

    def _init_ (self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
    def __str__(self):
        #Muestra los elementos de la linkedlist
        array = []
        nodo_actual = self.cabeza
        while nodo_actual != None :
               array.append(nodo_actual.valor)
               nodo_actual = nodo_actual.nodo_siguiente
        return str(array) + "Tamano : " + str(self.tamanio)

    def append (self, value):
        nuevo_nodo = self._Nodo(value)
        if self.cabeza == None and self.cola == None :
               self.cabeza = nuevo_nodo
               self.cola = nuevo_nodo
        else:
               self.cola.nodo_siguiente = nuevo_nodo
               self.cola = nuevo_nodo

        self.tamanio += 1

    def prepend (self, valor):
        #Agrega un nuevo elemento al principio de la linkedlist
        nuevo_nodo = self._Nodo(valor)
        if self.cabeza == None and self.cola == None:
               self.cabeza = nuevo_nodo
               self.cola = nuevo_nodo
        else :
               nuevo_nodo.nodo_siguiente = self.cabeza
               self.cabeza = nuevo_nodo

        self.tamanio += 1

    def shift (self):
        if self.tamanio == 0 :
               self.cabeza == None
               self.cola == None
        else:
               nodo_eliminado = self.cabeza
               self.cabeza = nodo_eliminado.nodo_siguiente
               nodo_eliminado.nodo_siguiente = None
               self.tamanio -= 1

               return print (f"El nodo eliminado tiene el valor {nodo_eliminado.valor}")

    def pop (self):
        #Saca el elemento de la linkedlist
        if self.tamanio == 0:
            self.cabeza = None
            self.cola = None
        else:
            nodo_actual = self.cabeza
            nueva_cola = nodo_actual
            while nodo_actual.nodo_siguiente != None :
                nueva_cola = nodo_actual
                nodo_actual = nodo_actual.nodo_siguiente
            self.cola = nueva_cola
            self.cola.nodo_siguiente = None
            self.tamanio -= 1
            return print (f"El valor eliminado es {nodo_actual.valor}")

    def get (self, indice):
        if indice == self.tamanio -1 :
            print (self.cola.valor)
            return self.cola
        elif indice == 0 :
            print (self.cabeza.valor)
            return self.cabeza
        elif not (indice >= self.tamanio or indice < 0 ):
            nodo_actual = self.cabeza
            contador = 0
            while contador != indice :
                nodo_actual = nodo_actual.nodo_siguiente
                contador += 1
            print (nodo_actual.valor)
            return nodo_actual
        else:
             return None

    def update (self,indice,valor):
        nodo_objetivo = self.get(indice)
        if nodo_objetivo != None :
            nodo_objetivo.valor = valor
        else :
            return None

    def insert (self,indice,valor):
        #Agrega un elemento en donde sea en la linkedlist dado el inidice
        if indice == self.tamanio -1 :
            return self.append (valor)
        elif not (indice >= self.tamanio or indice < 0 ):
            nuevo_nodo = self._Nodo(valor)
            nodos_anteriores = self.get(indice)
            nodos_siguientes = nodos_anteriores.nodo_siguiente
            nodos_anteriores.nodo_siguiente = nuevo_nodo
            nuevo_nodo.nodo_siguiente = nodos_siguientes
            self.tamanio += 1
        else:
             return None
    def remove (self,indice):
        #Saca un elemento de donde sea de la linkedlist dado el indice
        if indice == 0 :
            return self.shift()
        elif indice == self.tamanio- -1 :
            return self.pop()
        elif not (indice >= self.tamanio or indice < 0 ):
            nodos_anteriores = self.get(indice - 1)
            nodo_removido = nodos_anteriores.nodo_siguiente
            nodos_anteriores.nodo_siguiente = nodo_removido.nodo_siguiente
            nodo_removido.nodo_siguiente = None
            self.tamanio -= 1
            return nodo_removido
        else :
            return None

    def reverse (self):
        #Revierte la linked list
        nodos_revertidos = None
        nodo_actual = self.cabeza
        self.cola = nodo_actual
        while nodo_actual != None :
            nodo_siguiente = nodo_actual.nodo_siguiente
            nodo_actual.nodo_siguiente = nodos_revertidos
            nodos_revertidos = nodo_actual
            nodo_actual = nodo_siguiente
        self.cabeza = nodos_revertidos
        return self.cabeza






sll = Single_Linked_List()
sll.append(26)
sll.append(15)
sll.append(80)
sll.prepend(10)
print (sll)
sll.shift()
sll.insert(1,28)
print (sll)
sll.remove(1)
print (sll)
