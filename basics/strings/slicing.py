string1 = "O E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00, Ethernet2"
print(string1)
s = string1[5:15]   # starting at 5 up to but not including 15
print(s)

s = string1[5:]     # starting at 5 thru end of string
print(s)

s = string1[:10]    # from beginning up to but not including 10
print(s)

s = string1[:]      # entire string
print(s)

c = string1[-1]     # last char

c = string1[-2]     # 2nd to last char

s = string1[-9:-1]  # -9 from end up to but not including -1 from end
print(s)

s = string1[-5:]    # last 5 chars of string
print(s)

s = string1[:-5]    # all chars except last 5
print(s)

s = string1[::1]    # entire string
print(s)

s = string1[::-1]   # entire string, reverse order

s = string1[::2]    # print char skipping 2 chars til end of string (every other char)
print(s)

mystring = "0123456789"
c = mystring[0]
c = mystring[1]
c = mystring[9]

# Entire string
start = 0
stop = 10
step = 1
s = mystring[start:stop:step]
print(s)

# Even nums - skip 2 starting with 0
start = 0
stop = 10
step = 2
s = mystring[start:stop:step]
print(s)

# Odd nums - skip 2 starting with 1
start = 1
stop = 10
step = 2
s = mystring[start:stop:step]
print(s)

# 135
start = 1
stop = 7
step = 2
s = mystring[start:stop:step]
print(s)