class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def base_n(num10, n):
            str_n = ''
            while num10:
                if num10 % n >= 10:
                    return -1
                str_n += str(num10 % n)
                num10 //= n
            return int(str_n[::-1])
        
        p_flag = True
        for i in range(2, n + 1):
            base_n_str = str(base_n(n , i))
            #print(f'10 -> {i}, {i} -> {str_n}')
            if base_n_str == base_n_str[::-1]:
                pass
            else:
                p_flag = False
                break
        return p_flag

sol = Solution()
print(f'{sol.isStrictlyPalindromic(9)} expect False')
print(f'{sol.isStrictlyPalindromic(4)} expect False')