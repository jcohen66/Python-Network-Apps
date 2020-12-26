def my_first_function(x):
    "This is our first function!"
    print(x)

def my_sum(x, y, z):
    sum = x + y * z
    return sum ** 2

def my_sum_opt(x, y, z=3):
    sum = x + y * z
    return sum ** 2

def function1(x, *args):
    print(x)
    for argument in args:
        print(argument)

def function2(x, *kwargs):
    print(x)
    for argument in kwargs:
        print(argument)


# Positions
print(
    my_sum(1, 2, 3)
)

# Keyword
print(
    my_sum(x=1, y=2, z=3)
)

# Positional with Default by caller
print(
    my_sum(1, 2, z=3)
)

# Optional enforced by contract, no value
print(
    my_sum_opt(1, 2)
)

# Optional enforced by contract, with value
print(
    my_sum_opt(1, 2, 3)
)

# Positional with variable args, nothing passed
function1(1)

# Positional with variable args, values passed
function1("hello", 100, 200)
