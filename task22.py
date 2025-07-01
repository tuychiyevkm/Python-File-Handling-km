import csv

with open("Input/grades.csv") as f:
    reader = csv.DictReader(f)

    grade_n = int(0)

    for row in reader:
        grade = int( row[ "Grade" ] )
        
        if grade == 5: grade_n += 1

    result = f"The Number of '5' scored students is - {grade_n}"    

    with open( "Ouput/output22.txt", "w" ) as f2:
        f2.write(result)
        print(result)
