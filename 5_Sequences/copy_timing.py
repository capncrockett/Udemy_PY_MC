# The StackOverflow Python 3.6 Timings code to test copy.
import timeit

COUNT = 50000000
print("Array duplicating. Tests run", COUNT, "times")
setup = 'a = [0,1,2,3,4,5,6,7,8,9]; import copy'

print("b = list(a)\t\t", timeit.timeit(stmt='b = list(a)', setup=setup, number=COUNT))
print("b = copy.copy(a)\t", timeit.timeit(stmt='b = copy.copy(a)', setup=setup, number=COUNT))
print("b = a.copy()\t\t", timeit.timeit(stmt='b = a.copy()', setup=setup, number=COUNT))
print("b = a[:]\t\t", timeit.timeit(stmt='b = a[:]', setup=setup, number=COUNT))
print("b = a[0:len(a)]\t\t", timeit.timeit(stmt='b = a[0:len(a)]', setup=setup, number=COUNT))
print("*b, = a\t\t\t", timeit.timeit(stmt='*b, = a', setup=setup, number=COUNT))
print("b = []; b.extend(a)\t", timeit.timeit(stmt='b = []; b.extend(a)', setup=setup, number=COUNT))
print("b = []; for item in a: b.append(item)\t", timeit.timeit(stmt='b = []\nfor item in a:  b.append(item)', setup=setup, number=COUNT))
print("b = [i for i in a]\t", timeit.timeit(stmt='b = [i for i in a]', setup=setup, number=COUNT))
print("b = [*a]\t\t", timeit.timeit(stmt='b = [*a]', setup=setup, number=COUNT))
print("b = a * 1\t\t", timeit.timeit(stmt='b = a * 1', setup=setup, number=COUNT))
