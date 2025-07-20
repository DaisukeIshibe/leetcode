class Solution:
    def validStrings(self, n: int) -> list[str]:
        if n == 1:
            return ["0", "1"]

        m = 2 ** n
        out_list = []
        for i in range(m):
            if i == 0:
                continue
            bin_str = bin(i)[2:]
            len_str = len(bin_str)
            if len_str != n:
                for j in range(n - len_str):
                    bin_str = '0' + bin_str
            if '00' in bin_str:
                continue
            out_list.append(bin_str)
            print(f'{i} {bin_str}')
        return out_list

sol = Solution()
print(f'{sol.validStrings(3)} Expect ["010","011","101","110","111"]')
print(f'{sol.validStrings(2)} Expect ["01","10","11"]')
print(f'{sol.validStrings(5)} Expect ["01010","01011","01101","01110","01111","10101","10110","10111","11010","11011","11101","11110","11111"]')