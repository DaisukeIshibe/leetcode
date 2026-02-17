class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n_str = bin(n)[2:].zfill(32)  # 32ビットにパディング
        bin_n_rev = '0b' + bin_n_str[::-1]
        n_rev = int(bin_n_rev, 0)
        return n_rev


sol = Solution()
print(f'{sol.reverseBits(43261596)} expect 964176192')
print(f'{sol.reverseBits(2147483644)} expect 1073741822')