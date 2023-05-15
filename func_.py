def multiply(x, y):
    try:
        return x * y
    except TypeError:
        return f"The input must be a number"


# print(multiply("a", "b"))


# * args


def multiply_with_more_args(*lst):
    product = 1
    for num in lst:
        product *= num
    return product


s = [1, 23, 43, 56, 32, 78]


# print(multiply(3, 10, 5, 16))

# keyword argument
def get_user(**user):
    print(user)


# get_user(id=1, fname="micheal", lname="friday")


def investment(principal_amount, years):
    rate = 0.05
    try:
        for year in range(1, years + 1):
            roi = principal_amount * rate
            future_value = principal_amount + roi
            principal_amount = future_value
            print(f"year {year} return on investment is {roi}, your principal is now {future_value}")
    except TypeError:
        return "The amount cannot be a string"
    except ValueError:
        return "The value cannot be negative"
    finally:
        pass

investment("a", "f")
# investment(20000, 20)

