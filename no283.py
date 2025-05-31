def moveZeroes(nums: list[int]) -> None:
	nonzero_idx_list = [idx for idx, n in enumerate(nums) if n != 0]

	for i, n in enumerate(nonzero_idx_list):
		nums[i] = nums[n]

	for i in range(len(nonzero_idx_list), len(nums)):
		nums[i] = 0	
	print(nums)

# Test
nums = [0, 1, 0, 3, 12] # Output: [1, 3, 12, 0, 0]
print(moveZeroes(nums))