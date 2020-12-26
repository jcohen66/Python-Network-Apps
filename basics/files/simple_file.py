# files are cursors.  Once read, position
# moves and must be reset to go back.

# Modes
# 'r': open for reading (default)
# 'w': open for writing, truncating the file first
# 'x': open for exclusive creation, failing if the file already exists
# 'a': open for writing, appending to the end of the file if it exists
# 'b': binary mode
# 't': text mode (default)
# '+': open a disk file for updating (reading and writing)
# 'U': universal newlines mode (deprecated)

file_path = "C:\\Temp\Routers.txt"
file_mode = "r"             # w: write / a: append / b: binary
my_file = open(file_path, file_mode)

# Read next 5 bytes
text = my_file.read(5)
print(text)

# Read from cursor position to end
text = my_file.read()
print(text)

# Position the cursor at the end
my_file.tell()

# Position the cursor at the beginning
my_file.seek(0)

text = my_file.readline()
print(text)

my_file.seek(0)
list1 = my_file.readlines()
print(list1)

my_file.seek(0)
for line in my_file.readlines():
    if line.startswith("A"):
        print(line)

# Open for
my_file = open("C:\\Temp\Routers.txt", "x")

