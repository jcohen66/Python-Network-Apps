# immutable
# non-ordered
# duplicates allowed

my_tuple =(9, )     # must include ',' with single element

n = my_tuple[0]

tuple1 = ("Cisco", "2600", "12.6")      # tuple packing
(vendor, model, ios) = tuple1           # tuple unpacking

print(vendor)
print(model)
print(ios)

n = len(tuple1)

tuple2 = (1,4,2)
n = min(tuple2)
n = max(tuple2)
b = 2 in tuple2
b = 2 not in tuple2
del tuple2

my_tuple = (1, 2, 3, 'a', 'b', 'c', [4, 5, 6])
t = my_tuple[-1] * 5
print(t)
print(type(t))
