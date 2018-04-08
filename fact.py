# Dermot Kelleher - Excercise 6 - programming and scripting - 2018
# This program creates a function which outputs the factorial of a given number. 
# 04/03/2018
def factorial(x):
    for i in range(x-1, 1, -1): #The for loop goes from inputed number minus one down to zero
        x = x*i # The inputed number (x) is intially multiplied by x-1. Each result is then multipled by the next step in the for loop until the for loop reachs one.
    return x # Stops the function and returns a result which can then be called.

print("The factorial of 5 is", factorial(5)) # You input x and then call the result by printing it to the screen.
print("The factorial of 7 is", factorial(7))
print("The factorial of 10 is", factorial(10))
