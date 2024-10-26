def max_in_tuple(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

print(max_in_tuple((10, 20, 30, 40, 50)))
