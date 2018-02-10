# Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Kelleher"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# Exercise one forum post: My name is Dermot, so the first and last letter of my name (D + T = 4 + 20) give the number 24. The 24th Fibonacci number is 46,368. 

# Exercise two forum post: My surname is kelleher. 

# The first letter k is number 107

# The last letter r is number 114

# Fibonacci number 221 is 6867260041627791953052057353082063289320596021

# The ord() method returns the corresponding numeric code which represents the Unicode code point of that character.