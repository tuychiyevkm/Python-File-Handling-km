with open("Input/numbers.txt") as f:
  
    numbers=[line.strip() for line in f ]

sum = int(0)

for number in numbers:
    sum += int(number)

with open("Ouput/output02.txt","w") as f1:
    f1.write(f"The sum of numbers is - {sum}")

print(f"The sum of numbers is - {sum}")
