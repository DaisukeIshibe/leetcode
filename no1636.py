def frequencySort(self, nums: list[int]) -> list[int]:
	from collections import Counter

	# Count the frequency of each number
	freq = Counter(nums)

	# Sort the numbers first by frequency (ascending) and then by value (descending)
	sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))

	return sorted_nums

# Example usage:
print(frequencySort(None, [1, 1, 2, 2, 2, 3]))  # Output: [3, 1, 1, 2, 2, 2]