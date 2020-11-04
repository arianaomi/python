
numbers = [10, 20, 1, 10, 50, 50, 50, 20]

numbers_set = []

for number in numbers:
    if number in numbers_set:
        continue
    else:
        numbers_set.append(number)

print(numbers_set)
