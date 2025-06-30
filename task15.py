with open("Input/students.txt") as f:
    names=[line.strip() for line in f ]

with open("Ouput/output15.txt", "w") as f1:
    for name in names:
        f1.write(f"{name} - {len(name)}\n")
