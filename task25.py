import csv

with open("Input/grades.csv") as f:
    reader = csv.DictReader(f)

    with open( "Ouput/high_scores.csv", "w" ) as f1:
            for row in reader:
                grade = int( row[ "Grade" ] )
                name = row[ "Name" ]

                if grade == 5:
                    f1.write( name + "\n" )    
                    print(name )   


    # with open( "Ouput/output25.txt", "w" ) as f1:
    #     for row in reader:
    #         grade = int( row[ "Grade" ] )
    #         name = row[ "Name" ]

    #         if grade == 5:
    #             f1.write( name + "\n" )    
    #             print( name )   
        

