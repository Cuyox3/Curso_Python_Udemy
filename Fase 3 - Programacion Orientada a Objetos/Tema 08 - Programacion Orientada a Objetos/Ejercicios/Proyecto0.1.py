# Completa el ejercicio aquí
import math                             #La libreria math agrega funciones matematicas 
                                        #Como sqrt y se usa --> math.sqrt(int) (es una raiz cuadrada)

class Punto: 

    def __init__(self,x=0, y=0):          #Este es el constructor donde se inicializa el objeto
        self.x=x 
        self.y=y

    def Agregar_vector (self, x , y ):   #Esta funcion Crea los vectores y les añade  valores de x y y 
        print ("El vector no tiene valores") 
        return "El punto tiene coordenadas {} en x y {} en y ".format(self.x , self.y)
            
    def __str__ (self):                 #Toma dos vectores y calcula la resutante entre ambos
        return  "({} en x & {} en y)".format (self.x,self.y)

    def cuadrante (self):               #Te dice en que caudrante esta o si esta en el origen
        if self.x>0 and self.y>0:                  
             print("({} en x & {} en y)".format (self.x,self.y) + "Esta en el primer cuadrante")
        elif self.x<0 and self.y>0:                 
             print("({} en x & {} en y)".format (self.x,self.y) + "Esta en el segundo cuadrante")
        elif self.x>0 and self.y<0:                  
             print("({} en x & {} en y)".format (self.x,self.y) + "Esta en el tercer cuadrante")
        elif self.x<0 and self.y<0:                 
             print("({} en x & {} en y)".format (self.x,self.y) + "Esta en el cuarto cuadrante")
        elif self.x == 0 and self.y == 0 : 
             print("({} en x & {} en y)".format (self.x,self.y) + "Esta en el origen")
        return 
    
    def vector (self,p ):               #Toma dos vectores y calcula el resultado entre ambos 
        print ("El vector se encuentra entre {} y {} es ({},{})".format( self,p, p.x - self.x , p.y - self.y )) ## por que se ponen dos 
        return  
    
    def distacia (self,p):        
        distancia = math.sqrt ( ((p.y-self.y)^2) + ((p.x-self.x)^2) )            #Toma dos vectores y calcula la distancia entre ambos  
        print ("La distancia entre los puntos {} y {} es ".format(self, p , distancia))
        return 
     
A= Punto (2,3)
B= Punto (5,5)
C= Punto (-3,-1)
D= Punto (0,0) 

class Rectangulo :                      #La funcion abs() regresa el valor absoluto 

        def __init__(self) -> None:     #Crea los puntos, en caso de que no se pasen las coordenadas se creará el punto en el origen 
             pass
            
        def altrura () :                #Calcula la altura entre dos puntos 
             return 
         
        def ancho () :                  #Calcula el ancho de los dos puntos 
             return 
        
        def area ():                    #Calcula el area del rectangulo
             return