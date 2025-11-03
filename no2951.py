class Solution:
    def findPeaks(self, mountain: list[int]) -> list[int]:
        out_list = []
        for i in range(len(mountain) - 2):
            val0 = mountain[i]
            val1 = mountain[i + 1]
            val2 = mountain[i + 2]
            
            if val1 > val0:
                if val1 > val2:
                    out_list.append(i + 1)
            
        return out_list

sol = Solution()
print(f'{sol.findPeaks([2,4,4])} expect []')
print(f'{sol.findPeaks([1,4,3,8,5])} expect [1, 3]')