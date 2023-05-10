# unique value, no duplicate elements
set1 = {1, 2, 3, 3, 1, 2, 4, 1, 4}  # will give {1, 2, 3, 4}
set2 = {1, 5, 2, 6, 7, 10}
#  set methods
# add
# copy
# union

# union -> list common elements in both sets
print(set1 | set2)

# difference -> outputs only unique elements that is not in both sets
print(set1 - set2)

# intersection -> prints common elements in both sets
print(set1 & set2)

# disjoint -> print elements thats not present in both set
print(set1 ^ set2)

# set comprehension
set3 = {i for i in range(1, 21)}
