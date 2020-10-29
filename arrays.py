class Array:
    def __init__(self , tam):
        self.__info = [0 for x in range(tam)]

    def get_item( self , dato, posicion):
        dato = 0
        try:
            dato = self.__info[ posicion ]
        except Exception as e:
            print("Error de posicion")
            dato="Error"
        return dato

    def set_item (self , posicion):
            try:
                self.__info [posicion] =dato
            except Exception as e:
                print("Error de posicion")

    def get_length (self ):
        return len (self.__info)

    def clear (self, dato ):
        self.__info = [dato for x in range (len(self.__info))]

    def __iter__(self):
        return _IteradorArreglo( self.__info)

class IteradorArreglo:
    def __init__ (self , arr):
        self.__arr =arr
        self.__indice = 0

    def __iter__( self):
        return self

    def __next__ (self):
        if self.__indice <len(self.__arr):
            dato = self.__arr[self.__indice]
            self.__indice +=1
            return dato
        else:
            raise StopIteration


algo = Array (10)
print(algo.get_item(6363))
algo.set_item(555,3)
print (algo.get_item(3))
print(f"El arreglo tiene { algo.get_length() } elementos")
algo.clear(777)
print(algo.get_item(3))
print("--------")
for x in algo:
    print( x )
print("-----Prueba de iterador-----")
for x in range(algo.get_length()):
    print(f"{x}-> {algo.get_item(x)}")
