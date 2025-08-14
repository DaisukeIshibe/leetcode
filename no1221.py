class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count: int = 0
        count_rl = s.count('RL')
        count_lr = s.count('LR')
        return min(count_lr, count_rl)

sol = Solution()
print(f'{sol.balancedStringSplit("RLRRLLRLRL")} expect 4')
print(f'{sol.balancedStringSplit("RLRRRLLRLL")} expect 2')
print(f'{sol.balancedStringSplit("LLLLRRRR")} expect 1')