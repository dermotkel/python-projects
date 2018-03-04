# Dermot Kelleher - Excercise 6 - programming and scripting - 2018
# This program creates a function which outputs the factorial of a given number. 
# 04/03/2018
def factorial(x):
    y = 1 #The first number is multiplied by one to give itself.
    for i in range(x, 1, -1): #The for loop goes from the given number down to zero
        y = y*i # Each number is multiplied multipled by the previous answer until the for loop reachs 1.
    return y

print("The factorial of 5 is", factorial(5))
print("The factorial of 7 is", factorial(7))
print("The factorial of 10 is", factorial(10))