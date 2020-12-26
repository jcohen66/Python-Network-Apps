# dicts are unordered
# keys must be immutable
# keys must be same type
# values can be immutable or mutable

dict1 = {}
dict1 = {"Vendor": "Cisco", "Model": "2600", "IOS": "12.4", "Ports": "4"}

s = dict1['IOS']
s = dict1['Vendor']

dict1["RAM"] = "128"
dict1["IOS"] = "12.3"
del dict1["Ports"]

n = len(dict1)
b = "IOS" in dict1
b = "IOS" not in dict1

list1 = list(dict1.keys())
list2 = list(dict1.values())
list3 = dict1.items()       # returns key/value tuple
print(list3)

my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}
sorted_list = sorted(my_dict.values())

print(sorted_list)