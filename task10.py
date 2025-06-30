with open("Input/numbers.txt") as f:
    numbers = [ line.strip() for line in f ]

sorted_num = []

for number in numbers:
    sorted_num.append(int(number))

sorted_num.sort()
    
with open("Ouput/output10.txt", "w") as f1:
    for num in sorted_num:
        f1.write(f"{num}  ")

print(sorted_num)