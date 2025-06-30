with open("Input/students.txt") as f:
    names = f.readlines()

    names.sort(reverse=True)

with open("Ouput/output14.txt","w") as f1:
    f1.writelines(names)