a = 1
b = 2
a, b = b, a

lst = [25, 10, 15, 5, 30, 55, 35, 45, 20]

# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] > lst[j]:
#             lst[i], lst[j], = lst[j], lst[i]

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


student_records = [
    {"id": 1, "name": "Rotimi", "score": (50, 70, 80)},
    {"id": 2, "name": "David", "score": (50, 70, 80)},
    {"id": 3, "name": "Timi", "score": (50, 70, 80)},
    {"id": 4, "name": "Mariam", "score": (50, 70, 80)},
    {"id": 5, "name": "Esther", "score": (50, 70, 80)},
]

student_records.append({"id": 6, "name": "Awwal", "score": (50, 70, 80)})
student_records.append({"id": 7, "name": "Dele", "score": (50, 70, 80)})
# print(student_records)
student_records.pop(3)


# print(student_records)


# def duplicate(dlst: list):
#     a
#     no_duplicate = set(dlst)
#     if len(no_duplicate) != len(dlst):
#         print("there's duplicate")
#     else:
#         print("There's no duplicate")


# def duplicate2(lzt: list):
#     for item in lzt:
#         if lzt.count(item) > 1:
#             print(f"The item {item} occurred more than once")
#         else:
#             print(f"There's no duplicate")


# file = open("account.txt", mode='r')
# file.write("1001 sikiru 50000\n")
# file.write("1002 adewunmi 50000\n")
# file.write("1001 asa 50000\n")
# file.close()


def username_generator(email: str):
    username = email.split("@")[0]
    return f"Your username is {username}"


# print(username_generator("ayinladesikiru@gmail.com"))


x = {
    "name": "Asa",
    "age": 27,
    "status": "married",
    "isOnline": True,
    "hobbies": ['politics', 'coding', 'football'],
    "fashion": {},
}
