list1 = []
type(list)      # list

list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]

n = len(list1)
s = list1[0]
s = list1[1]
s = list1[2]
n = list1[3]
n = list1[-2]
n = list1[-1]
# n = list1[100]      # IndexError
list1[2] = "HP"
list1.append(100)
del list1[4]
list1.pop(0)         # removes first element
list1.remove("Juniper")

list1.insert(2, "Nortel")       # as the new [2] element

print(list1)

# Note single no type mixing otherwise returns TypeError
list2 = [2, -11,  12]

n = min(list2)
n = max(list2)

list1.extend(list2)     # Tacks on list2 to the end of list 1
print(list1)

list1.append(10)        # Tacks on to end of list1

n = list1.count(10)
print(n)

print(list2)
print(id(list2))
list2.sort()            # reorders in place
print(list2)
print(id(list2))        # same

list2.reverse()         # reorders in place

list3 = sorted(list2, reverse = True)   # returns a copy of the list
print(id(list2))
print(id(list3))

list3 = list1 + list2
print(list3)

list3 = list1 * 2

print(list3)