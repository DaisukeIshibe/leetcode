class Solution:
    def minimumFlips(self, n: int) -> int:
        n_bin_str = bin(n)[2:]
        rev_n_bin = n_bin_str[::-1]
        diff_count:int = 0
        for a, b in zip(n_bin_str, rev_n_bin):
            if a != b:
                diff_count += 1
        return diff_count

sol = Solution()
print(f'{sol.minimumFlips(7)} expect 0')
print(f'{sol.minimumFlips(10)} expect 4')