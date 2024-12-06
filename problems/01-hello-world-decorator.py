# Implement a decorator function called `hello_world_decorator` that
# will be used to `print` statements. The decorator function should
# take another function argument as a callback, implement an inner
# wrapper function, and finally return the wrapper function object.

# Implement the inner wrapper function with the following:
# - A print statement of the string "Hello"
# - Calls the callback function

# - Another print statement after the callback containing the string
# - "Goodnight"

# Finally, be sure to decorate the `world` function using the
# decorator syntax.


# Write your function here.
def hello_world_decorator(func):
    def inner_func():
        print("Hello")
        func()
        print("goodbye")

    return inner_func


# when you call the world function, it'll be passed in to the hello
# world decorator and the function that is returned from that will be
# assigned to "world"
@hello_world_decorator
def world():
    print("World")


world()  # > Hello World Goodnight
