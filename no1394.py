class Solution:
    def findLucky(self, arr: list[int]) -> int:
        n_dict: dict = {}
        for a in arr:
            if not a in n_dict:
                n_dict[a] = 1
            else:
                n_dict[a] += 1

        lucky_list = [k for k, v in n_dict.items() if k == v]
        if lucky_list == []:
            return -1
        else:
            return max(lucky_list)


sol = Solution()
print(f'{sol.findLucky([2,2,3,4])} expect 2')
print(f'{sol.findLucky([1,2,2,3,3,3])} expect 3')
print(f'{sol.findLucky([2,2,2,3,3])} expect -1')
print(f'{sol.findLucky([19,12,11,14,18,8,6,6,13,9,8,3,10,10,1,10,5,12,13,13,9])} expect 1')