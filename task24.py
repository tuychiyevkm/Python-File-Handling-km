import csv

with open("Input/grades.csv") as f:
    reader = list(csv.DictReader(f))

    gr_t = int(0)
    gr_n = int(0)


    for row in reader:
        grade = int( row[ "Grade" ] )
        gr_t += grade
        gr_n += 1 

    with open( "Ouput/output24.txt", "w" ) as f1:

        for  row in reader:
             grade = int( row[ "Grade" ] )
             name = row[ "Name" ]

             if grade > (gr_t/gr_n):

                f1.write( name + "\n" )    
                print( name )   
