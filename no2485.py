class Solution:
    def pivotInteger(self, n: int) -> int:
        f_list = [i for i in range(1, n + 1)]
        sum_f_list = []
        for i in range(len(f_list)):
            if i == 0:
                sum_f_list.append(f_list[i])
            else:
                sum_f_list.append(sum_f_list[i - 1] + f_list[i])
                 
        l_list = [i for i in range(n, 0, -1)]
        sum_l_list = []
        for i in range(len(l_list)):
            if i == 0:
                sum_l_list.append(l_list[i])
            else:
                sum_l_list.append(sum_l_list[i - 1] + l_list[i])
        sum_l_list.reverse()
        for a, b in zip(sum_f_list, sum_l_list):
            if a == b:
                return sum_l_list.index(a) + 1
        
        return -1

sol = Solution()
print(f'{sol.pivotInteger(8)} expect 6')
print(f'{sol.pivotInteger(1)} expect 1')
print(f'{sol.pivotInteger(4)} expect -1')