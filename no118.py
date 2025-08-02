class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        out_list = [[1]]
        if numRows == 1:
            return out_list
        
        for i in range(numRows):
            if len(i) == 1:
                out_list
            pass
        return [[]]

sol = Solution()
print(f'{sol.generate(5)} expect [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]')
print(f'{sol.generate(1)} expect [[1]]')