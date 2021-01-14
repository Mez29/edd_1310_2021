def  factorial ( n ):
    si  n  ==  0 :
        volver  1
    otra cosa :
        retorno  factorial ( n  -  1 ) *  n

def  printRev ( n ): # 3
    si  n  >  0 :
        printRev ( n  -  1 )
        imprimir ( n )

def  fibonacci ( n ):
    si  n  ==  1  o  n  ==  0 :
        volver  n
    si  n  >  1 :
        retorno ( fibonacci ( n - 1 ) +  fibonacci ( n - 2 ))

def  main ():
    para  num  en  rango ( 1 , 11 , 1 ):
        r  =  factorial ( num )
        print ( f "El factorial de {  num  } es {  r  } " )

def  main2 ():
    printRev ( 3 )

def  main3 ():
    para  num  en  rango ( 11 ):
        print ( str ( fibonacci ( num )) +  "," , end = "" )
    imprimir ( "" )

main3 ()
