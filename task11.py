f = open("Input/students.txt")
names = f.readlines()

f1 = open ("ouput/output11.txt","w")
f1.writelines(names)