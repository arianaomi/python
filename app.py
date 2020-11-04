
# Data type -> Dictionary (tipo mapa)

my_dictionary = {
    "name":"Naomi",
    "last_name":"Puertos",
    "age":24
}

print(my_dictionary)

key = my_dictionary.keys()
print(key)
values = my_dictionary.values()
print(values)
items_count = my_dictionary.items()
print(items_count)

my_dictionary.update({"gender":"female"})

for key,value in items_count:
    print(value)