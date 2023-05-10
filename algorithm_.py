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



# def fizzbuzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return "FizzBuzz"
#     if n % 3 == 0:
#         return "Fizz"
#     if n % 5 == 0:
#         return "Buzz"


# print(fizzbuzz(15))

























