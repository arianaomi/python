number = int(input("Ingresa un número"))
factorial = 1

for i in range(1, number):
    factorial *= (i+1)
print(factorial)
