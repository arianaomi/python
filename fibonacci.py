
limit = int(input("Cuántos elementos? "))
n1, n2 = 0, 1
fibonacci = []

for n in range(limit):
    if(n == 0 or n == 1):
        fibonacci.append(1)
    else:
        total = fibonacci[n-2] + fibonacci[n-1]
        fibonacci.append(total)

print(fibonacci)
