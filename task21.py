import csv 

with open( "Input/grades.csv") as f:
    reader =  csv.DictReader(f)

    max_gr = int(0)

    for row in reader:
        grade = int( row[ "Grade" ] )
        
        if grade > max_gr:
            max_gr = grade

    result = f"The highest grade is - {max_gr}"

    with open( "Ouput/output21.txt", "w" ) as f1:
        f1.write(result)
        print(result)