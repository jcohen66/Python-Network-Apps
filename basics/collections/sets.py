# unordered by default
# no dups

list4 = [1,2,3,4,5,2,3]
print(id(list4))

list5 = set(list4)
print(id(list5))

set1 = set([1,2,3])
print(type(set1))

set1 = [1, 2, 3]
print(type(set1))

set1 = {1, 1, 2, 2, 3}
print(set1)
print(type(set1))

b = 1 in set1
b = 10 not in set1

set1.add(10)
set1.add(10)        # adding 2nd time is silent fail.  no error
set1.remove(10)

set1 = {1, 2, 3, 4}
set2 = {3, 5, 8}

set3 = set1.intersection(set2)      # Both have
print(set3)

set3 = set1.difference(set2)        # in set1 not in set2
print(set3)

set3 = set2.difference(set1)        # in set2 not in set1
print(set3)

set3 = set1.union(set2)             # uniques combined from both
print(set3)

set1.pop()                          # removes [0] element
set1.clear()                        # removes all elements

list1 = [1, 2, 3, 4]
list2 = [3, 4, 7]

# Immutable
fs1 = frozenset(list1)
fs2 = frozenset(list2)

fs3 = fs1.intersection(fs2)
fs3 = fs1.difference(fs2)
fs3 = fs1.union(fs2)

