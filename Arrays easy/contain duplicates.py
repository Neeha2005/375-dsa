#using sets
def containsDuplicate(nums):
    nums2 = set(nums)
    if len(nums2) != len(nums):
        return True
    else:
        return False
nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))