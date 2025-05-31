def productExceptSelf_(nums: list[int]) -> list[int]:
	result_list: list = [1] * len(nums)
	len_num = len(nums)

	for i in range(len_num):
		for j in range(len_num):
			if i != j:
				if nums[j] == 1:
					pass
				elif nums[j] == -1:
					result_list[i] = -result_list[i]
				else:
					result_list[i] *= nums[j]
	
	return result_list

def productExceptSelf(nums: list[int]) -> list[int]:
	len_num = len(nums)
	mult_left_list = [1] * len_num
	for idx in range(len_num):
		if idx == 0:
			mult_left_list[idx] = nums[idx]
		else:
			mult_left_list[idx] = mult_left_list[idx - 1] * nums[idx]

	mult_right_list = [1] * len_num
	for idx in range(len_num - 1, -1, -1):
		if idx == len_num - 1:
			mult_right_list[idx] = nums[idx]
		else:
			mult_right_list[idx] = mult_right_list[idx + 1] * nums[idx]
	
	print(mult_left_list, mult_right_list)
	result_list = [0] * len_num
	for idx in range(len_num):
		if idx == 0:
			result_list[idx] = mult_right_list[idx + 1]
		elif idx == len_num - 1:
			result_list[idx] = mult_left_list[idx - 1]
		else:
			result_list[idx] = mult_left_list[idx - 1] * mult_right_list[idx + 1]
	return result_list

n_llist = [1, 2, 3, 4] # [24, 12, 8, 6]
print(productExceptSelf(n_llist))