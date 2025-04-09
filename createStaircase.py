""" 
Problem:  take a list as argument and return a list of sublists creating a staircase,
if can't be done return false
ex: list = [1,2,3,4,5,6]
staircase = [[1], [2, 3], [4, 5, 6]]
"""

def create_staircase(nums):
    while len(nums) != 0:
        step = 1
        subsets = []
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False
    return subsets

def create_staircase2(nums):
    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False
    return subsets
list = [1,2,3,4,5,6]
print(create_staircase(list))
print(create_staircase2(list))