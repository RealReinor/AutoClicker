def set_var():
    my_var = 10  # Local variable inside the function
    print(f"Inside set_var: {my_var}")


def use_global_var():
    global my_var
    print(f"Inside use_global_var: {my_var}")


set_var()
use_global_var()  # This will raise an error
