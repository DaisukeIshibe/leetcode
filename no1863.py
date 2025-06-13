class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        import itertools
        total_sum:int = 0
        for i in range(1, len(nums) + 1):
            for subset_list in itertools.combinations(nums, i):
                xor_sum = 0
                for num in subset_list:
                    xor_sum ^= num
                #print(f'Current subset: {subset_list}, XOR sum: {xor_sum}')
                total_sum += xor_sum
        return total_sum

sol = Solution()
nums = [1, 3]
print(sol.subsetXORSum(nums))  # Output: 6
nums = [3,4,5,6,7,8]
print(sol.subsetXORSum(nums))  # Output: 480