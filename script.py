# polynomial evaluation
eq = "x**3 + x**2 + x + 1"
x = 1
ans = eval(eq)
print (ans)


# lambda function
x = lambda x,y:x+y
print(x(10,20))

# reduce function
# The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say [1,2,3] and you have to find its sum.
from functools import reduce
reduce(lambda x, y : x + y,[1,2,3])

# define an initial value
reduce(lambda x, y : x + y, [1,2,3], -3)

