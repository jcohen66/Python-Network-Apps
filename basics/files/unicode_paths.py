# Windows has trouble with unicode characters
# Must either escape or use raw string literal preface

# escape
f = open("C:\\Temp\\Routers.txt", "r")

# raw string literal
f = open(r"C:\Temp\Routers.txt", "r")


