def reverse_array(idx, nums):
    if idx == len(nums) //2:
        return
    swap_idx = len(nums) - 1 - idx
    nums[idx], nums[swap_idx] = nums[swap_idx], nums[idx]
    reverse_array(idx + 1, nums)


nums = input().split()
reverse_array(0,nums)
print(" ".join(nums))