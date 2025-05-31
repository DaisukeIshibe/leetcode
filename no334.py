def increasingTriplet(nums: list[int]) -> bool:
	if len(nums) < 3:
		return False

	nums_dict = {n:idx for idx, n in enumerate(nums)}
	sorted_nums = sorted(nums)
	len_nums = len(nums)

	print(nums_dict)
	for n in sorted_nums:
		start_pos = nums_dict[n] + 1
		for c in range(start_pos, len_nums):
			if nums[c] > n:
				for d in range(c + 1, len_nums):
					if nums[d] > nums[c]:
						return True

	return False

nums0 = [1, 2, 3, 4, 5] # True
nums1 = [5, 4, 3, 2, 1] # False
nums2 = [2,1,5,0,4,6] # True
nums3 = [20,100,10,12,5,13] # True
nums4 = [6,7,1,2] # False
nums5 = [1, 2, 1, 3] # True
#print(f'{nums0} act = {increasingTriplet(nums0)} expect = True')
#print(f'{nums1} act = {increasingTriplet(nums1)} expect = False')
#print(f'{nums2} act = {increasingTriplet(nums2)} expect = True')
#print(f'{nums3} act = {increasingTriplet(nums3)} expect = True')
#print(f'{nums4} act = {increasingTriplet(nums4)} expect = False')
print(f'{nums5} act = {increasingTriplet(nums5)} expect = True')
# The above code is a brute force solution with O(n^2) time complexity.