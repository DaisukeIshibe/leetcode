class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        def n2bin(n):
            bin_num = '0b'+str(n)
            return int(bin_num, 0)
        
        dec_dict = {n2bin(n):True for n in nums}
        max_len = max([len(n) for n in nums])
        max_str = '0b'+''.join(['1'] * max_len)
        max_int = int(max_str, 0)
        for i in range(max_int):
            if i in dec_dict:
                pass
            else:
                str_bin = str(bin(i)[2:])
                len_str_bin = len(str_bin)
                if len_str_bin == max_len:
                    return str_bin
                else:
                    str_bin = '0' * (max_len - len_str_bin) + str_bin
                    return str_bin
        
        return '0'

sol = Solution()
print(f'{sol.findDifferentBinaryString(["01","10"])}')
print(f'{sol.findDifferentBinaryString(["00","01"])}')
print(f'{sol.findDifferentBinaryString(["111","011","001"])}')