# Dermot Kelleher - Excercise 5 - programming and scripting - 2018
# This program outputs the first four variables from the Iris database using formatting 
# 02/03/2018
with open("data/iris.csv") as f:
    for line in f:
        f = line.split(',')[:4] # This creates a list with only the first four variables.
        f = [float(i) for i in f]# The above process creates a string and Gerhard on the course forum shows that you must convert the string to a float. This creates a new list with the values as floats. 
        f = ('{:.1f} {:.1f} {:.1f} {:.1f}'.format(f[0], f[1], f[2], f[3])) # This formating creates a list storing the values with one decimel place. Cite: https://mkaz.tech/code/python-string-format-cookbook/
        print(f)

        
        


                
