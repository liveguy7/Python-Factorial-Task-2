#Recursive Function to find the Factorial of a Number

def factorial(n):
  if n == 0 or n == 1:
      return 1
  else:
      return n * factorial(n-1)


num = int(input("Enter a number: "))
print("The Factorial of {0} is {1}".format(num, factorial(num)))

