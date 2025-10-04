class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count: int = 0
        dist_dict = {'L': 0, 'R': 0}
        sub_str: str = ''
        for c in s:
            dist_dict[c] += 1
            sub_str += c
            if dist_dict['L'] == dist_dict['R']:
                count += 1
                dist_dict['L'] = 0
                dist_dict['R'] = 0
        return count

sol = Solution()
print(f'{sol.balancedStringSplit("RLRRLLRLRL")} expect 4')
print(f'{sol.balancedStringSplit("RLRRRLLRLL")} expect 2')
print(f'{sol.balancedStringSplit("LLLLRRRR")} expect 1')