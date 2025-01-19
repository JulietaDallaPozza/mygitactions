def hello():
    greeting = "hi"
    return greeting


def bye():
    farewell = "bye"
    return farewell


print(greeting)  # Error: NameError - 'greeting' is not defined outside hello()
