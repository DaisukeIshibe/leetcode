class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        nums_str = ''.join([str(n) for n in nums])
        len_list = [len(n) for n in nums_str.split('0')]
        if len(len_list) == 1:
            return len(nums) - 1
        
        max_len = max(len_list)
        max_bit_str = '1' * max_len
        index_pos = nums_str.index(max_bit_str)
        if index_pos == 0:
            # Pre position
            pass
            # Next position
            nxt_index = index_pos + max_len
            if nums[index_pos + max_len] == 0:
                pass
        elif index_pos:
            # Pre position
            pass
            # Next position
            pass
        
        print(nums, max_bit_str, nums_str, index_pos)
        return 0

sol = Solution()
print(f'{sol.longestSubarray([1,1,0,1])} expect 3')
print(f'{sol.longestSubarray([0,1,1,1,0,1,1,0,1])} expect 5')
print(f'{sol.longestSubarray([1,1,1])} expect 2')
print(f'{sol.longestSubarray([1,1,0,0,1,0,1,0,0,1])} expect 2')