with open("Input/numbers.txt") as f:
    numbers = [ line.strip() for line in f]

sq_num = []

for number in numbers:
    sq_num.append(int(number)**2)

with open("Ouput/output07.txt", "w") as f1:
    for num in sq_num:
        f1.write(f"{num}  ")

print(sq_num)