import random
nums = []
for i in range(25):
    x = random.randint(1, 100)
    if x not in nums and x < 50:
        nums.append(x)
print(nums)
nums.sort()
nums.pop()
nums.pop()
nums.pop()
del nums[0]
print(f"The final list is {nums}")