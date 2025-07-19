class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        import itertools
        len_t = len(tiles)
        t_list = list(tiles)
        total_list = []
        for i in range(len_t):
            combi_list = list(set(itertools.combinations(t_list, i+1)))
            for combi in combi_list:
                c_list = list(set(list(itertools.permutations(combi, len(combi)))))
                total_list.extend(c_list)
        return len(set(total_list))

sol = Solution()

print(f'{sol.numTilePossibilities("AAB")} Expect 8')
print(f'{sol.numTilePossibilities("AAABBC")} Expect 188')
print(f'{sol.numTilePossibilities("V")} Expect 1')
print(f'{sol.numTilePossibilities("CDC")} Expect 8')