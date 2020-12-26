
def my_var_func():
    # local namespace
    my_var_f = 10
    print(my_var_f)
    return my_var_f

def my_var_func_global():
    # global namespace
    global my_var_f
    print(my_var_f)

# built-in namespace
print(list(range(10)))

# global namespace
my_var = 10
print(my_var)

result = my_var_func()
my_var_f = 20
my_var_func_global()
print(result * 10)

