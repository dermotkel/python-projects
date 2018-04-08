# Dermot Kelleher - Excercise 4 - programming and scripting - 2018
# This program is a solution for Project Euler problem 5

# Project Euler problem 5: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? Cite: https://projecteuler.net/problem=5
# 01/03/2018 

for i in range(2520, 9999999999, 2520): # The answer must be a multiple of 2520. You can start at 2520 and step the for loop by 2520 for a fast answer. Cite: http://jasoncampos.blogspot.ie/2011/06/project-euler-5-java.html 
    if (i % 11 == 0 and i % 13 == 0 and i % 14 == 0 and i % 16 == 0 # Instead of dividing by every number from 1 to 20, we can leave out numbers as follows: Cite: https://blog.dreamshire.com/project-euler-5-solution/
         and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0): # The form i % n == 0 finds if the remainder of i divided by a number is equal to zero. 
         print(i)
         break # stops the loop as soon as the smallest result is found. 
         
