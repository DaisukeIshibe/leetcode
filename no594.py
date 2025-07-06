class Solution:
	def findLHS(self, nums: list[int]) -> int:
		n_dict = {}
		for n in nums:
			if not n in n_dict:
				n_dict[n] = 1
			else:
				n_dict[n] += 1
        
		max_len = 0
		n_list = sorted(n_dict.keys())
		for i in range(len(n_list) - 1):
			next = n_list[i + 1]
			curr = n_list[i]
			diff = next - curr
			if diff == 1:
				interm = n_dict[curr] + n_dict[next]
				if interm > max_len:
					max_len = interm
		
		#print(n_list, min_val, max_len)
		return max_len
    
sol = Solution()

print(f'{sol.findLHS([1,3,2,2,5,2,3,7])} expect 5')
print(f'{sol.findLHS([1,2,3,4])} expect 2')
print(f'{sol.findLHS([1,1,1,1])} expect 0')
print(f'{sol.findLHS([1,2,2,3,4,5,1,1,1,1])} expect 7')
print(f'{sol.findLHS([1,3,5,7,9,11,13,15,17])} expect 0')
print(f'{sol.findLHS([1,2,3,3,1,-14,13,4])} expect 3')