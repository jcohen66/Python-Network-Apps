x = 10
y = 0

if x == 5 and type(x) == int:
    y = 5
elif x == 10 and type(x) == int:
    y == 10


vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

for each_vendor in vendors:
    print(each_vendor)

my_string = "Cisco"

for letter in my_string:
    print(letter)
    print(letter * 2)
    print(letter * 3)

r = range(10)
for i in r:
    print(i * 2)

n = len(vendors)
list = list(range(5))
print(list)

for element_index in range(len(vendors)):
    print(vendors[element_index])

for index, element in enumerate(vendors):
    print(index, element)

for element in vendors:
    print(element)
else:
    print("The end of the list has been reached")


