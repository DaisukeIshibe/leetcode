class Solution:
    def minOperations(self, n: int) -> int:
        n_list = [i*2 + 1 for i in range(n)]
        average = sum(n_list) / len(n_list)
        abs_list = [abs(i - average) for i in n_list]
        ope_num = sum(abs_list) // 2
        #print(f'{n_list} average {average} abs {abs_list} ope_num {ope_num}')
        return int(ope_num)

sol = Solution()
print(f'{sol.minOperations(3)} expect 2')
print(f'{sol.minOperations(6)} expect 9')