my_list = [1, 2, 3, 4, 5, 6, 7]

for element in my_list:
    print(element)

my_iter = iter(my_list)
print(type(my_iter))

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter))  # this one will throw StopIteration

# Generatpr
def my_gen(x, y):
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield i * y

my_object = my_gen(10, 5)
print(type(my_object))
next(my_object)
next(my_object)
next(my_object)
next(my_object)
next(my_object)
next(my_object)
next(my_object)
next(my_object)


gen_exp = (x for x in range(5))
print(type(gen_exp))
print(gen_exp)

from itertools import *

list1 = [1, 2, 3, 'a', 'b', 'c']
list2 = [101, 102, 103, 'X', 'Y']

c = chain(list1, list2)

for i in chain(list1, list2):
    print(i)

for i in count(10, 2.5):
    if i <= 50:
        print(i)
    else:
        break


list1 = list(filterfalse(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7]))
print(list1)


range(10)
list(range(10))
list1 = list(range(10))[2:9:2]
print(list1)

list1 = list(islice(range(10), 2, 9, 2))
print(list1)