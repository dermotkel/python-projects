# Dermot Kelleher - Excercise 6 - programming and scripting - 2018
# This program creates a function which outputs the factorial of a given number. 
# 04/03/2018
def factorial(x):
    for i in range(x-1, 1, -1): #The for loop goes from inputed number minus one down to zero
        x = x*i # Each number is multiplied multipled by the previous answer until the for loop reachs one.
    return x

print("The factorial of 5 is", factorial(5))
print("The factorial of 7 is", factorial(7))
print("The factorial of 10 is", factorial(10))
