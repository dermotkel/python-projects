# Dermot Kelleher 01/03/2018 Exercise 4

# Project Euler problem 5: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? Cite: https://projecteuler.net/problem=5

for i in range(2520, 9999999999, 2520): # The answer must be a multiple of 2520. Cite: http://jasoncampos.blogspot.ie/2011/06/project-euler-5-java.html
    if (i % 11 == 0 and i % 13 == 0 and i % 14 == 0 and i % 16 == 0 # We can leave out numbers as follows: Cite: Some factors can be removed, so we do not have to use all numbers from 1 to 20. Cite: https://blog.dreamshire.com/project-euler-5-solution/
         and i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and i % 20 == 0): 
         print(i)
         break # stops the loop as soon as the smallest result is found. 
         