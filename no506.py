class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        sorted_list = sorted(score, reverse=True)
        order_dict = {i:idx for idx, i in enumerate(sorted_list)}
        out_list = []
        for s in score:
            if order_dict[s] == 0:
                out_list.append("Gold Medal")
            elif order_dict[s] == 1:
                out_list.append("Silver Medal")
            elif order_dict[s] == 2:
                out_list.append("Bronze Medal")
            else:
                out_list.append(str(order_dict[s] + 1))
        return out_list

sol = Solution()
print(f'{sol.findRelativeRanks([5,4,3,2,1])} expect ["Gold Medal","Silver Medal","Bronze Medal","4","5"]')
print(f'{sol.findRelativeRanks([10,3,8,9,4])} expect ["Gold Medal","5","Bronze Medal","Silver Medal","4"]')