from csv import DictReader
from collections import Counter

grades = []
count_g = {}
with open("Input/grades.csv") as f:
    reader = DictReader(f)

    for row in reader:
        grade = int( row[ "Grade" ] )
        grades.append(grade)

    count_g = Counter(grades)
    with open("Ouput/output23.txt", "w" ) as f1:
        f1.write(str(dict(count_g)))

print(count_g)
