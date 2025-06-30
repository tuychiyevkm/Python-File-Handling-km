with open("Input/numbers.txt") as f:
    numbers = [ line.strip() for line in f]
    
even_num = []

for number in numbers:
    if int(number) % 2 == 0: 
        even_num.append(number)

with open("Ouput/output04.txt", "w") as f1:
    for num in even_num:
        f1.write(F"{num}  ")

print(even_num)

