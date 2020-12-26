x = 1

while x <= 10:
    print(x)
    x = x + 1
else:
    print("x is now greater than 10")

x = "Cisco"
if ("i" in x) and (len(x) > 3):
    print(x, len(x))

list1 = [4, 5, 6]

list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        print(i * j)
    print(i)

x = 1

while x <= 10:
    z = 5
    x += 1
    while z <= 10:
        print(z)
        z += 1

for number in range(10):
    if 5 <= number <= 9:
        print(number)

list1 = [4, 5, 6]
list2 = [10, 20, 30]

for i in list1:
    for j in list2:
        if j == 20:
            break
        print(i * j)
    print("Outside the nested loop")

for i in list1:
    for j in list2:
        if j == 20:
            continue
        print(i * j)
    print("Outside the nested loop")