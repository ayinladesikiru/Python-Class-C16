my_list = []
# name = ["sultan", "mariam", "torin", "awwal", "david"]
# students = [["sulatan", 35, 200, 90.9], ["mariam", 32, 200, 95.0]]
# print(students[0])
# ones = [1] * 100
# # print(ones)
# list2 = students + name
# # print(name[::-1])
#
# even_number = list(range(0, 51, 2))
#
# print(even_number)

numbers = [1, 2, 3, 4, 5]
# x = numbers[0]
# y = numbers[1]
# z = numbers[2]
# a = numbers[3]
# b = numbers[4]
x, y, *others = numbers
print(x, y, others)

letters = ["a", "b", "c", "d", "e"]
# letters1 = list("abcd")

# for index, letter in enumerate(letters):
#     print(index, letter)

letters.insert(0, "z")
letters.remove("z")
# del letters[0:2]
letters.pop()
print(letters)

even_num = []
for number in range(21):
    if number % 2 == 0:
        even_num.append(number)

even_num2 = [i for i in range(21) if i % 2 != 0]

print(even_num)
print(even_num2)

set1 = {1, "a", 2, {1, "0", 1}, {0, 1}}

dict1 = {"a": 1}

