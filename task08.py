with open("Input/numbers.txt") as f:
    numbers =[ line.strip() for line in f ]

mul_num = []

for number in numbers:
    if int(number) % 5 == 0: 
        mul_num.append(int(number))

with open("Ouput/output08.txt", "w") as f1:
    for num in mul_num:
        f1.write(f"{num}  ")

    f1.write(f"\nThe number of multiples of 5 is - {len(mul_num)}")

    print(mul_num, "\n In total:",len(mul_num) )