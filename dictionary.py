# key value pari
# performs better for faster optimization because elements can be located by using their key.

# declaring a dictionary
dictionary1 = {}  # empty dictionary
dictionary2 = {"id": 1, "name": "sultan", "age": 21}

# using the build in dict function
dictionary3 = dict(a=1, b=2)

# dictionary has methods like pop, item, copy , values, keys, get etc

# dictionary comprehension
x = {x: x ** 2 for x in range(1, 21)}
print(x)