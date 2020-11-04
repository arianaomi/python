string = input("Ingresa una cadena ")
lowers = []
uppers = []
order_string = ''


for character in string:
    if character.islower():
        lowers.append(character)
    else:
        uppers.append(character)

lowers.extend(uppers)
print(order_string.join(lowers))