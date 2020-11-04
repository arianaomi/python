
# Tipo de datos

# String
word = 'Hola mundo'
phrase = "Da igual"

# Number
integer_number = 20
float_number = 20.2
complex_number = 1j

# list -> colección de varios datos
lista = [1, 2, 3]
list_copy = lista.copy()  # copiar una lista
lista.append(4)  # Agregar valores a la lista al final(Cambia original)
lista.clear()  # elimina todos los items
count = lista.count(2)  # saber cuantas veces se repite un elemento

print('first_element', list_copy[0])
print('Elements in list_copy: ', len(list_copy))
#print(word, phrase, integer_number, float_number, complex_number)

# Metodos de una lista
lista = ['Naomi', "Hola", "Mundo", "Kira", "Groovy"]
lista.pop()  # Elimina el ultimo elemento de la lista
lista.remove('Mundo')  # Elimina uno elemento por su valor
lista.reverse()
lista.sort()  # es case-sensitive

print(lista)

# Tuple -> no se pueden modificar(dif con la lista), solo tiene dos metodos
tupla = ('hola', 'mundo', 'somos', 'tupla')

print(tupla.count('hola'))
print(tupla.index('hola'))  # Regresa el indice donde se encuentra

# Range -> un numero inicial a un numero final
rango = range(6)
print(rango)

# Dictionary
kira_dictionary = {
    "key": "value",
    "name": "Kira",
    "age": 6
}

print(kira_dictionary)
print(kira_dictionary['name'])
print(kira_dictionary.get('name'))  # acceder al valor
kira_dictionary["name"] = "Shakira"  # cambiar un valor

kira_dictionary["barks"] = 'yes'  # Agrega un elemento
#! kira_copy = kira_dictionary.copy()  # copia
kira_copy = dict(kira_dictionary)  # copia
kira_dictionary.pop('key')  # Elimina un elemento
kira_dictionary.popitem()  # Elimina el ultimo item agregado


print('len dictionary:', len(kira_dictionary))
print(kira_dictionary)
print(kira_copy)

kira = {
    "age": 4,
    "specie": "mestiza"
}

groovy = {
    "age": 8,
    "specie": "bobtail"
}

pets = {
    "kira": kira,
    "groovy": groovy
}

# constructor dict
mascotas = dict(nombre="Gala", edad=7)

print(mascotas)

# recorrer un diccionario
for key in pets:
    print('pets', pets[key])


for key, values in pets.items():
    print('hi', key, values)

print("name" in pets)
# booleano

verdadero = True
falso = False

print(verdadero, falso)
