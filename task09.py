with open("Input/numbers.txt") as f:
    numbers = [ line.strip() for line in f ]

with open("Ouput/output09.txt", "w") as f1:
    for num in numbers:
        f1.write(f"{int(num)} -> {len(num)}\n" )
