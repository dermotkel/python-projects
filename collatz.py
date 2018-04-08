# Dermot Kelleher - Excercise 3 - programming and scripting - 2018
# This program outputs the Collatz Conjecture of a given integer 
# 10/02/2018
i = int(input("Please enter an integer: ")) # Asks the user to input an integer and stores it as i
print(i) # prints the inputed integer to the beginning of the list
while i != 1:  # Loop will continue until i is one
    if i % 2 == 0: # If i is even, divide by two
        i = i/2 
        i = int(i) # converts the results into an integer - removes the decimals
        print(i)
    elif i % 2 != 0: # If i is not even multiply by 3 and add one
        i = (i*3)+1
        i = int(i)
        print(i)
    
