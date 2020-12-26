my_string = 'Cisco Switch'

# Forward - 0 based
c = a[0]

# Backward - 1 based
c = a[-1]

n = my_string.index("i")    # first position

n = my_string.count("i")    # occurrences

n = my_string.find("sco")       # first index of or -1 if not found

s = my_string.lower()
s = my_string.upper()

b = my_string.startswith("C")
b = my_string.endswith("h")

my_string2 = "   Cisco Switch    "

s = my_string2.strip()   # remove spaces
s = my_string2.strip("$")
s = my_string2.replace(" ", "")

my_string3 = "Cisco,Juniper,HP,Avaya,Nortel"
a = my_string3.split(",")   # returns array

s = "_".join(my_string)     # inserts a "_" between each char






