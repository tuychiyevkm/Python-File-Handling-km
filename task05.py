with open("Input/numbers.txt") as f:
    numbers = [ line.strip() for line in f]

avg_num = int(0)

for num in numbers:
    avg_num += int(num)

avg_num = avg_num / len(numbers)

with open("Ouput/output05.txt", "w") as f1:
    f1.write(F"The average of the numbers is - {avg_num}")

print(avg_num)