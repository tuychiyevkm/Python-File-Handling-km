input_name = str(input("Type a name:"))
name_l = input_name.lower()

with open("Input/students.txt") as f:
    names = [line.strip().lower() for line in f if line.strip()]


with open("Ouput/output18.txt","w") as f1:
     
    if name_l in names:   
        f1.write(f"The name - {input_name} is  on the list ")

    else:
         f1.write(f"The name - {input_name} is not on the list ")


    print("The answer has written in output18.txt")