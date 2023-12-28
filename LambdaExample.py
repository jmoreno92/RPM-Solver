# Example using lambda
# Reference: https://www.w3schools.com/python/python_lambda.asp

def myfunc(n):
  return lambda a: a * n

# Alternative 1
mydoubler = myfunc(2)
print(mydoubler(11))

# Alternative 2
print(myfunc(2)(11))
