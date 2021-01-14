numbers = [1, 2, 2, 5, 43, 2, 3, 5, 1, 55, 67, 7, 8, 7]
unique = []
print(set(numbers))

for every_number in range(len(numbers)):
    if numbers[every_number] not in unique:
        unique.append(numbers[every_number])

print(unique)