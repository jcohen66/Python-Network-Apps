my_str = "You can learn any programming language, whether it is Python2, Python3, Perl, Java, javascript or PHP"

import re

a = re.match("Xou", my_str)         # returns match or None
print(a)

# case sensitive match
a = re.match("You", my_str)
print(a.group())

# case insensitive match
a = re.match("you", my_str, re.I)
print(a.group())


my_str = "can learn You any programming language, whether it is Python2, Python3, Perl, Java, javascript or PHP"

# case insensitive match
a = re.match("you", my_str, re.I)
print(type(a))      # NoneType

# Search anywhere in string
arp = "22.22.22.1   0     b4:a9:5a:ff:c8:45 VLAN#222        L"

# Pay attention to group borders to adjust greediness
a = re.search(r"(.+?) +(\d) +(.+?)\s{2,} (\w) *", arp)
print(a.group(1))
print(a.group(2))
print(a.group(3))
print(a.group(4))
print(a.groups())

# Find List of all patterns matched
a = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)
print(a)
to
arp = "22.22.22.1   0     b4:a9:5a:ff:c8:45 VLAN#222    10.10.10.10    L"
a = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)
print(a)

# Replace all occurrences with supplied value
arp = "22.22.22.1   0     b4:a9:5a:ff:c8:45 VLAN#222        L"
b = re.sub(r"\d", "7", arp)
print(b)
