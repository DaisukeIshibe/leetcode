class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        nums_str = ''.join([str(n) for n in nums])
        len_list = [len(n) for n in nums_str.split('0')]
        if len(len_list) == 1:
            return len(nums) - 1

        max_len = max(len_list)
        #max_bit_str = '1' * max_len

        max_index = len_list.index(max_len)
        nxt_index = max_index + 1
        if max_index == 0:
            #print(nums_str, len_list)
            return max_len + len_list[nxt_index]
        if nxt_index >= len(len_list):
            #print(nums_str, len_list)
            max_len = 0
            for i in range(len(len_list) - 1):
                sum_len = len_list[i] + len_list[i + 1]
                if max_len < sum_len:
                    max_len = sum_len
            return max_len

        max_len = 0
        for i in range(len(len_list) - 1):
            sum_len = len_list[i] + len_list[i + 1]
            if max_len < sum_len:
                max_len = sum_len
        #print(len_list)
        return max_len


sol = Solution()
print(f'{sol.longestSubarray([1,1,0,1])} expect 3')
print(f'{sol.longestSubarray([0,1,1,1,0,1,1,0,1])} expect 5')
print(f'{sol.longestSubarray([1,1,1])} expect 2')
print(f'{sol.longestSubarray([1,1,0,0,1,0,1,0,0,1])} expect 2')
print(f'{sol.longestSubarray([1,1,0,0,1,1,1,0,1])} expect 4')
print(f'{sol.longestSubarray([0,0,1,1])} expect 2')
print(f'{sol.longestSubarray([1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,0,1,1,1,1])} expect 14')
print(f'{sol.longestSubarray([1,1,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,0,1,0,1,1,1,1,1])} expect 9')
print(f'{sol.longestSubarray([1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1])} expect 15')
print(f'{sol.longestSubarray([1,1,1,0,1,1,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,1,0,0,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1,0,0,1,1,1,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1])} expect 8')