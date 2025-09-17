def second_largest(nums):
    nums=list(set(nums))
    if len(nums)<2:
        return None
    nums.sort()
    return nums[-2]
nums=[25,50,76,34,24]
print(second_largest(nums))