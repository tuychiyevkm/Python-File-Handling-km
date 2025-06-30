with open("Input/students.txt") as f:
    names = [ line.strip() for line in f ]


with open("Ouput/output16.txt","w") as f1:

    for name in names:
        if len (name) > 5:
            f1.write (f"{name}\n")