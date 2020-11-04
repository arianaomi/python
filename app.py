
# Data type -> List (colección de elementos del mismo o dif tipo de dato)

my_list = ['perro','gato','caballo','perro']

for animal in my_list:
    print(animal)

# Method List
my_list.append('pato') #agregar nuevo elemento
print(my_list)
my_list.remove('perro') #elimina el primero que encuentre
print(my_list)
#agregar varios elementos al final:
my_list.extend(['gato','tortuga'])
print(my_list)
#agregar elementos en la posicion deseada
my_list.insert(0,"puerquito")
print(my_list)