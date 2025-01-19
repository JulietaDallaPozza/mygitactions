def hello():
    greeting = "hi"
    return greeting  # Returning greeting to make it accessible outside


def bye():
    farewell = "bye"
    return farewell


print(hello())  # This works because `hello()` now returns the greeting
