
# Functions -> bloque de código reutilizable

def suma(numer_1 = 0, number_2 = 0):
    print("Hola soy una funcion, necesito los :")
    return numer_1 + number_2

resultado = suma(2,4)
print(str(resultado)) #print espera un string se necesita convertir 

def resta(numer_1,number_2):
    return numer_1 - number_2

resultado = resta(number_2=5 , numer_1=10)
print(str(resultado))

def sumatoria(*numbers): # * para recibir el numero de parametros que sean
    for number in numbers:
        print(str(number))

sumatoria(1,3,45,6,7)

# Clases 
class Beer :
    def __init__(self,name) : # constructor por default init y como parametro a si mismo, otros parametros
        self.name = name
    
    def añejar(self,time = 1): #dandole un tiempo por default
        print('Tu cerveza se ha añejado en el tiempo ' +str(time) + ' días de nombre ' + self.name ) #accediendo a variables del constructor

my_beer = Beer("Modelo") # automaticamente recibe self y no necesita la palabra new
print(my_beer.name)
my_beer.añejar(10)

#Programación funcional -> menos código

lista = range(5) # Regresa una lista de n elementos

for i in lista:
    print(i)

# listas  por compresa

lista_multiplicada_por_1000 =[i * 1000 for i in range(10)] 
print(lista_multiplicada_por_1000)

#Funciones lambda : lambda parametros: retorna 

#variables que guardan una funcion 

multiplica = lambda a,b : a*b
resultado = multiplica(2,8)
print (resultado)
