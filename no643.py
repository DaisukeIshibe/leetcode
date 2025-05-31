def findMaxAverage(nums: list[int], k: int) -> float:
	len_nums = len(nums)
	# Integral array
	int_list = [0] * len_nums
	for i in range(len_nums):
		if i == 0:
			int_list[0] = nums[i]
		else:
			int_list[i] = int_list[i - 1] + nums[i]

	#print(int_list)  # Debug: print the integral array
	# Calculate sum
	max_s: int = 0
	for i in range(len_nums - k + 1):
		s:int = 0
		if i == 0:
			s = int_list[k - 1]
			max_s = s
		else:
			s = int_list[i + k - 1] - int_list[i - 1]
			if s > max_s:
				max_s = s
	
	return max_s / k

nums = [1, 12, -5, -6, 50, 3]
k = 4 # Output: 12.75
print(findMaxAverage(nums, k))