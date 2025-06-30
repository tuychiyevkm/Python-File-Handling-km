with  open("Input/students.txt" ) as f:
    names = [line.strip() for line in f if line.strip()]

# Method 1

names_a = [name for name in names if name.upper().startswith("A")]

with open("Ouput/output17.txt", "w") as f1:

    for name in names_a:
        f1.write(f"{name}\n")

# Method 2

# with open("Ouput/output17.txt", "w") as f2:

#     for name in names:
#         if name.upper().startswith("A"):
#             f2.write(f"{name}\n")

