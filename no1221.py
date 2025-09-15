class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count: int = 0
        sub_len = len(s) // 2
        for i in range(sub_len, 0, -1):
            sub_rl = 'R' * i + 'L' * i
            sub_lr = 'L' * i + 'R' * i
            c = s.count(sub_rl)
            if c > 0:
                count += c
                s = s.replace(sub_rl, '|')
                print(f'Match {sub_rl} -> {s}')
            c = s.count(sub_lr)
            if c > 0:
                count += c
                s = s.replace(sub_lr, '|')
                print(f'Match {sub_lr} -> {s}')
        return count

sol = Solution()
print(f'{sol.balancedStringSplit("RLRRLLRLRL")} expect 4')
print(f'{sol.balancedStringSplit("RLRRRLLRLL")} expect 2')
print(f'{sol.balancedStringSplit("LLLLRRRR")} expect 1')