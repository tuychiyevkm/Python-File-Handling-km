import csv

with open("Input/grades.csv") as f:
    reader = csv.DictReader( f )

    gr_t = int(0)
    gr_n = int(0)


    for row in reader:
        grade = int( row[ "Grade" ] )
        gr_t += grade
        gr_n += 1 

    result = f"GPA ( Grade Point Average ) : {round(gr_t/gr_n, 1)}"

    with open( "Ouput/output20.txt", "w" ) as f1:
        f1.write(result)
        print(result)
        
        
        
