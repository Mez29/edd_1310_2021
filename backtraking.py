from Array2d import Array2d

class LaberintoADT:
    """
    0 pasillo, 1 pared, S salida y E entrada
    pasillo es una tupla ((2,1), (2,2), (2,3), (2,4), (3,2),(4,2))
    """
    def __init__(self , rens, cols, pasillos ):
        self.__laberinto= Array2d(rens, cols, '1')
        for pasillo in pasillos:
            self.__laberinto.set_item( pasillo[0], pasillo[1], '0')

    def to_string (self):
        self.__laberinto.to_string()
