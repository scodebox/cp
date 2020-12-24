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

# define an initial value  https://stackoverflow.com/questions/409370/sorting-and-grouping-nested-lists-in-python?answertab=votes#tab-top
reduce(lambda x, y : x + y, [1,2,3], -3)

# Sorting and Grouping Nested Lists in Python
x = [
 ['4', '21', '1', '14', '2008-10-24 15:42:58'], 
 ['3', '22', '4', '2somename', '2008-10-24 15:22:03'], 
 ['5', '21', '3', '19', '2008-10-24 15:45:45'], 
 ['6', '21', '1', '1somename', '2008-10-24 15:45:49'], 
 ['7', '22', '3', '2somename', '2008-10-24 15:45:51']
]

from operator import itemgetter

x.sort(key=itemgetter(1))
