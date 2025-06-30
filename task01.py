with open("Input/numbers.txt") as f:
    
    numbers = [line.strip() for line in f]

with open("Ouput/output01.txt","w") as f2:

    for number in numbers:
        number = int(number)
        f2.writelines(f"{number}  ")
print(numbers)