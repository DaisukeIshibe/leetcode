class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i_dict: dict = {}
        for i in range(len(num) - 2):
            curr = num[i]
            next = num[i + 1]
            nxt3 = num[i + 2]
            if curr == next:
                if next == nxt3:
                    str_ = curr * 3
                    i_dict[str_] = int(str_) 
        
        sorted_list = sorted(i_dict.items(), key=lambda x:x[1])
        if sorted_list == []:
            return ''
        else:
            return sorted_list[-1][0]


sol = Solution()
print(f'{sol.largestGoodInteger("6777133339")} expect "777"')
print(f'{sol.largestGoodInteger("2300019")} expect "000"')
print(f'{sol.largestGoodInteger("42352338")} expect ""')
print(f'{sol.largestGoodInteger("222")} expect "222"')