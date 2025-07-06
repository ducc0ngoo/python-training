"""
list []

index: must be int

positive index
0 first value
len - 1 last value

negative index
last value: -1
first value: -len
"""
nums = [1, 3, 2, 2, 1]
nums.append(100)
nums.extend([3, 4, 5])

print(nums)
nums.insert(1, -100)

print(nums)
nums.append(100)
nums.remove(100)

print(nums.pop(2))

del nums[1]

print(nums)

nums.sort(reverse=True)

print(nums)

new_list = nums.copy()
print(new_list is nums)
print(id(new_list), id(nums))
print(new_list == nums)

print(nums.count(1000))
print(nums.index(100))

nums.reverse()
print(nums)

nums.clear()
print(nums)
print(id(nums))
# nums = nums + [3]
nums += [3]
print(id(nums))
print(nums)
