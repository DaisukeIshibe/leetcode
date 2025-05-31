def triangleType(self, nums: list[int]) -> str:
	len_set = len(set(nums))
	if len_set == 1:
		return "equilateral"
	elif len_set == 2:
		nums_dict:dict = {}
		for n in nums:
			if not n in nums_dict:
				nums_dict[n] = 1
			else:
				nums_dict[n] += 1
		
		print(nums_dict)
		mono_num = [k for k, v in nums_dict.items() if v == 1][0]
		doub_num = [k for k, v in nums_dict.items() if v == 2][0]

		if mono_num < (doub_num * 2):
			return "isosceles"
		else:
			return None

	else:
		max_n = max(nums)
		min_n = min(nums)
		nums.remove(max_n)
		nums.remove(min_n)
		mid_n = nums.pop()

		if max_n >= (min_n + mid_n):
			return None
		else:
			return "scalene"

s = [9, 4, 9]
print(f's = {s} act = {triangleType(None, s)} expect = "isosceles"')