import csv  

with open( "Input/grades.csv" ) as f:
    reader = csv.DictReader(f)

    with open( "Ouput/output19.txt", "w" ) as f1:
        for row in reader:
            name = row[ "Name" ]
            grade = row[ "Grade" ]
            
            text = F"Student: {name}, Grade: {grade}"

            print( text )
            f1.write( text + "\n" )


