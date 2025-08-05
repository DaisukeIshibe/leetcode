from collections import Counter

class Solution:
	def findMatrix(self, nums: list[int]) -> list[list[int]]:
		# ヒント: collections.Counterを使うとカウントが高速
		# また、各数字の出現回数分だけ空リストを用意し、各回目に数字を割り当てると効率的
		count = Counter(nums)
		max_freq = max(count.values())
		res = [[] for _ in range(max_freq)]
		for num, freq in count.items():
			for i in range(freq):
				res[i].append(num)
		return res

sol = Solution()
nums = [1,3,4,1,2,3,1]
expect = [[1,3,4,2],[1,3],[1]]
print(f'{sol.findMatrix(nums)} expect {expect}')

nums = [1,2,3,4]
expect = [[4,3,2,1]]
print(f'{sol.findMatrix(nums)} expect {expect}')