# Dermot Kelleher - Excercise 3 - programming and scripting - 2018
# This program outputs the Collatz Conjecture of a given integer 
# 10/02/2018
i = int(input("Please enter an integer: "))
# prints the inputed integer to the beginning of the list
print(i)
while i != 1:
    if i % 2 == 0:
        i = i/2
# converts the results into an integer - removes the decimals 
        i = int(i)
        print(i)
    elif i % 2 != 0:
        i = (i*3)+1
        i = int(i)
        print(i)
    
