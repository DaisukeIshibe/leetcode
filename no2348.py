class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        sub_list = []
        zero_list = []
        len_nums = len(nums)
        for i in range(len_nums):
            cur_n = nums[i]
            if cur_n == 0:
                sub_list.append(0)
            else:
                if sub_list != []:
                    zero_list.append(len(sub_list))
                sub_list = []
        if sub_list != []:
            zero_list.append(len(sub_list))
        
        #print(zero_list)
        total = 0
        for z in zero_list:
            sub_total = 0
            for i in range(1, z + 1):
                sub_total += i
            total += sub_total
        return total


sol = Solution()
print(f'{sol.zeroFilledSubarray([1,3,0,0,2,0,0,4])} expect 6')
print(f'{sol.zeroFilledSubarray([0,0,0,2,0,0])} expect 9')
print(f'{sol.zeroFilledSubarray([2,10,2019])} expect 0')