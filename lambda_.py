list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def odd_value(n):
#     if n % 2 != 0:
#         return n


ans = list(map(lambda x: x ** 2, list3))
print(ans)

print(list(filter(lambda n: n % 2 != 0, list3)))
