with open("Input/students.txt") as f:
    names = f.readlines()

l = len(names)

with open("Ouput/output12.txt","w") as f1:
    f1.writelines(names)
    f1.write(f"\nIsmlar soni: {l}")