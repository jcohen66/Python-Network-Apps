# lambda arg1, arg2, ... , argn: an expression using the arguments

a = lambda x, y: x * y
print(a(2, 10))
print(a(5, 50))

def my_func(my_list):
    list_xy = []
    for x in range(10):
        for y in range(5):
            result = x * y
            list_xy.append(result)
    return list_xy + my_list

print(my_func([100, 101, 102]))

# same as
b = lambda my_list: [x * y for x in range(10) for y in range(5)] + my_list

def product10(a):
    return a * 10

r1 = range(10)

iter = list(map(product10, r1))
for n in iter:
    print(n)

list1 = list(map((lambda a: a * 10), r1))
print(list1)

filter((lambda a: a > 5), r1)
list1 = list(filter((lambda a: a > 5), r1))
print(list1)