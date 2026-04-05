import random
import math

def leer_numero (ini,fin,mensaje): 
    while True: 
        try: 
            valor= int(input(mensaje))
        except: 
            print("Error: Numero no valido")
        else: 
            if valor >=ini and valor <= fin : 
                break
    return valor


    
def generador (): 
    numeros = leer_numero(1,20,"Cuantos numeros quieres generar del [1-20]\n")
    modo = leer_numero(1,3,"'Como quieres redondear los numeros:\n[1]Al alza \n[2]A la baja \n[3]Normal\n")

    lista = []

    for i in range(numeros): 
        numeros = random.uniform(0,101)
        if modo == 1 : 
            print ("{} = {}".format(numeros,math.ceil(numeros)))
            numeros = math.ceil(numeros)

        elif modo == 2 : 
            print ("{} = {}".format(numeros,math.floor(numeros)))
            numeros = math.floor(numeros)
        
        elif modo == 3 : 
            print ("{} = {}".format(numeros,round(numeros)))
            numeros = round(numeros)
    
    return lista 

generador()