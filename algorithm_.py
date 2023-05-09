a = 1
b = 2
a, b = b, a

lst = [25, 10, 15, 5, 30, 55, 35, 45, 20]

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j], = lst[j], lst[i]

# print(lst)
# print(lst.sort())

# set1 = {6, 2, 5, 4, 1}
# print(sorted(set1))


# lst1 = [i for i in range(1, 21) if i % 2 == 0]
# print(lst1)


# for x in range(10):
#     print("hello C16")

# doubles = {}
# for a in range(1, 11):
#     doubles[a] = a ** 2

from sys import getsizeof
#
double = [a ** 2 for a in range(1000000)]
doubles = (a ** 2 for a in range(1000000))
print(getsizeof(double))
print(getsizeof(doubles))

# def fizzbuzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return "FizzBuzz"
#     if n % 3 == 0:
#         return "Fizz"
#     if n % 5 == 0:
#         return "Buzz"


# print(fizzbuzz(15))


# list2 = [1, 2, 3, 4, 5, 6]
#
#
# def square(n):
#     return n ** 2
#
#
# ans = list(map(square, list2))
# print(ans)



#
# def odd_num(lzt):
#     odd = []
#     for n in lzt:
#         if n % 2 != 0:
#             odd.append(n)
#
#     return odd
#
#
# print(odd_num(list3))

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def odd_value(n):
    if n % 2 != 0:
        return n


# print(list(filter(odd_value, list3)))


# browsing_history = []
# browsing_history.append("google.com")
# browsing_history.append("semicolon.africa")
# browsing_history.append("linkedln.com")
# print(browsing_history)
# browsing_history.pop()
# print(browsing_history)
# print(f"redirecting to {browsing_history[-1]}")
# if not browsing_history:
#     print("back button disabled")
























