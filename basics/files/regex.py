import re

# \d digit
# \s whitespace
# \w word (letters, numbers, underscore)
# \D any non-digit char
# \S any non-whitespace char
# \W any non-word (letters, numbers, underscore)
# \A specified char
# \Z ends with char


a = "I enjoy learning programming languages such as Python 3"

result = re.search(r"\D+", a)
print(result.group())

result = re.search(r"\S+", a)
print(result.group())

result = re.search(r"\W+", a)
print(result.group())
print(a.index(result.group()))

result = re.search(r"\AI", a)
print(result.group())

result = re.search(r"3\Z", a)
print(result.group())
print(a.index(result.group()))


# sets of chars
result = re.findall(r"[a-z]", a)
print(result)

# range
result = re.findall(r"[A-Z]", a)
print(result)

# range
result = re.findall(r"[a-d]", a)
print(result)

# range
result = re.findall(r"[a-z]", a)
print(result)

# specific chars
result = re.findall(r"[abn]", a)
print(result)

# all chars except 'a'
result = re.findall(r"[^a]", a)
print(result)

# any digit
result = re.findall(r"[0-9]", a)
print(result)

# range
result = re.findall(r"[1-5]", a)
print(result)

#range
result = re.findall(r"[135]", a)
print(result)

# all except
result = re.findall(r"[^7]", a)
print(result)

# or conditional, first passes so second not tested
result = re.search(r"\W(\w{2})\W|([A-Z]\w{5})\s\d", a)
print(result.groups())

# or conditional, first fails so second is tested
result = re.search(r"\W(\w{50})\W|([A-Z]\w{5})\s\d", a)
print(result.groups())

# split into list
result = re.split(r" ", a)
print(result)

# split into list
result = re.split(r"\s", a)
print(result)

# same as
result = a.split(" ")
print(result)

# determine delimiter
result = re.split(r"\W\w{2}\W", a)
print(result)

# Replace all and return num of replacements
tuple1 = re.subn(r"\s", "_", a)
print(tuple1)

# starts with
result = re.search(r"^[A-Z]\s\w{5}", a)
print(result)

# ends with
result = re.search(r"[A-Z]\w{5}\s\d$", a)
print(result)

x = "He is ... zzzzzzzzzz ... sleeeeeeping"

# Find repetitions, non-greedy
result = re.search(r"z{1,10}", x)
print(result)

# Find repetitions, non-greedy
result = re.search(r"z{3,10}", x)
print(result)



