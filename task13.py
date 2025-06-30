f1 = open("input/students.txt")
names=f1.readlines()
names.sort()

f2=open("ouput/output13.txt","w")
f2.writelines(names)
