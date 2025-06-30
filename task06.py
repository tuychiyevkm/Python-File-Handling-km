with open("Input/numbers.txt") as f:
    numbers = [ line.strip() for line in f]

odd_num = []

for number in numbers:
    if int(number) % 2 == 1:
        odd_num.append(int(number))


with open("Ouput/odd_numbers.txt", "w") as f1:
    for num in odd_num:
        f1.write(F"{num}  ")

with open("Ouput/output06.txt", "w") as f1:
    for num in odd_num:
        f1.write(F"{num}  ")

# print(odd_num)