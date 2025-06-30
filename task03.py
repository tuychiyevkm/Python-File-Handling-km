with open("Input/numbers.txt") as f:
    numbers = [line.strip() for line in f] 

big_num = int(0)

for number in numbers:
    if int(number) > big_num: big_num = int(number)

with open("Ouput/output03.txt", "w") as f1:
    f1.write(f"The biggest number in this list is - {big_num}")

print(big_num)
