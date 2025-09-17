class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        len_arr = len(arr)
        len_list = [i for i in range(1, len_arr + 1) if i % 2 == 1]
        total = 0
        for len_ in len_list:
            for i in range(0, len_arr - len_ + 1):
                sub_arr = arr[i:i+len_]
                total += sum(sub_arr)
        return total


sol = Solution()
print(f'{sol.sumOddLengthSubarrays([1,4,2,5,3])} expect 58')
print(f'{sol.sumOddLengthSubarrays([1,2])} expect 3')
print(f'{sol.sumOddLengthSubarrays([10,11,12])} expect 66')