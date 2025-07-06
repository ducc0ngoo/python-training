"""
for loops
"""
"""



0 3



1 3
"""
# index: 0 -> 9 = range(len(names))
# 10 -> len(names)
#           0        1      2     3      4       5      6      7      8      9
# Hoang = hOANG
# names = ["Hoang", "Minh", "mom", "b", "Khoa", "Dang", "beu", "xit", "ba", "Dung"]
# names.append("son")
#
# for i in range(len(names)):
#     if i % 2 == 0:
#         print(i, names[i].swapcase())
a = [1, 2, 3] # value
#   [2, 4, 6]
#    0  1  2    index
for i in range(len(a)):
    a[i] = a[i]*2

# for value in a:
#     print(value, end=" ")

print(*a)
