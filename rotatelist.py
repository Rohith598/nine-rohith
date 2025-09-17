def rotate_list(nums,k):
    n=len(nums)
    if nums==0:
        return nums
    k=k%n
    return nums[-k:]+nums[:-k]
nums=[0,9,8,7,6,5,4,3,2,1]
k=4
print(rotate_list(nums,k))