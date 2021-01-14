def cuenta_regresiva(n):
    print(n, end=" ,  ")
    if n > 0:
        return cuenta_regresiva(n-1)

def main():
    print("1er ejercicio. Cuenta regresiva: \n")
    cuenta_regresiva(5)


from pila_recursividad import Stack
pila = Stack()
pila_2 = Stack()

def half_stack(mitad):
    if pila.lenght()>0:
        if pila.lenght()!= mitad:
            pila_2.push(pila.pop())
            half_stack(mitad)
        elif pila.lenght()==mitad:
            i = pila.pop()
            print(f"\n {i} es el elemento en la posicion media de la pila.")
            for elem in range(pila_2.lenght()):
                pila.push(pila_2.pop())
            print("\nResultado:")
            return pila.to_string()
    elif pila.lenght()==0:
        print("La pila esta vacia, inserte elementos.")

def half(size):
    mitad = int(pila.lenght()/2)
    residuo = pila.lenght()%2
    if residuo == 0:
        return int(mitad)
    else:
        mitad = mitad + residuo
        return int(mitad)

def main2():
    print("\n 2do Ejercicio. Seleccione los elementos medios de una pila: ")
    pila.push(1)
    pila.push(2)
    pila.push(3)
    pila.push(4)
    pila.push(5)
    pila.push(6)
    pila.push(7)
    pila.push(8)
    pila.push(9)
    pila.to_string()
    #print(f"Hay {pila.lenght()} elementos .  ")
    size = pila.lenght()
    mitad = half(size)
    half_stack(mitad)

main()
main2()
