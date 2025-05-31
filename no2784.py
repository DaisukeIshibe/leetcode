def isGood(nums: list[int]) -> bool:
	len_num = len(nums)
	sorted_list = sorted(nums)

	if sorted_list[len_num - 1] == sorted_list[len_num - 2]:
		if sorted_list[len_num - 1] + 1 == len_num:
			uniq_list = list(set(sorted_list[:len_num - 1]))
			print(f'uniq_list = {uniq_list} sorted_list = {sorted_list}')
			if len(uniq_list) == len_num -1:
				return True
			else:
				return False
		else:
			return False
	else:
		return False

print(isGood([1, 3, 3, 2])) # True