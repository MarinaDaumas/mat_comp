
def centered_average(nums):
    nums.sort()
    centered_nums = nums[1:-1:]
    result = sum(centered_nums)/len(centered_nums)
    return result
    
centered_average([89, 4, 33, 6, 8, 64,21, 2])