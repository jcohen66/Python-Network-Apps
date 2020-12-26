# Overwrite
new_file = open("C:\\Temp\\newfile.txt", "w")
num_chars = new_file.write("I like Python!\nDo you?")
new_file.close()

# Overwrite
new_file = open("C:\\Temp\\newfile.txt", "w")
num_chars = new_file.write("This is a great day for science!")
new_file.close()

# Overwrite
new_file = open("C:\\Temp\\newfile.txt", "w")
num_chars = new_file.writelines(["Cisco", "Juniper", "HP"])
new_file.close()

# Overwrite
new_file = open("C:\\Temp\\newfile.txt", "w")
num_chars = new_file.writelines(("Cisco1", "Juniper1", "HP1"))
new_file.close()

# Overwrite
new_file = open("C:\\Temp\\newfile.txt", "w")
num_chars = new_file.writelines(("Cisco1", "Juniper1", "HP1"))
new_file.close()

# Overwrite
new_file = open("C:\\Temp\\newfile.txt", "a")
num_chars = new_file.writelines(["This line has been appended"])
new_file.close()

# Read and Write
new_file = open("C:\\Temp\\newfile.txt", "w+")
num_chars = new_file.write("Something else!")

new_file.seek(0)
text = new_file.read()
print(text)
new_file.close()


# Close automatically
with open("C:\\Temp\\newfile.txt", "w") as f:
    f.write("Hello Python!")

if f.closed:
    print("The file was closed automatically")
else:
    print("The file is still open.")