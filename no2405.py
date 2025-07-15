class Solution:
    def partitionString(self, s: str) -> int:
        uniq_max_num = len(set(s))
        if uniq_max_num == 1:
            return len(s)

        s_list = [s]
        total = 0        
        # Find the longest frame
        break_flag = False
        for uniq_num in range(uniq_max_num, 1, -1):
            for idx, s_ in enumerate(s_list):
                for i in range(len(s_) - uniq_num + 1):
                    phrase = s_[i:i+uniq_num]
                    if len(set(phrase)) == uniq_num:
                        s0 = s_[0:i]
                        s1 = s_[i+uniq_num:len(s)]
                        s_list.pop(idx)
                        s_list.append(s0)
                        s_list.append(s1)
                        total += 1
                        print(f'unique {uniq_num} {phrase} Update->{s}')
                        break_flag = True
                        break
            if break_flag:
                break
        
        return total + len(s)


sol = Solution()
s = "abacaba"
ret = sol.partitionString(s)
expect = 4
status = 'OK' if ret == expect else 'NG'
print(f'{ret} {expect} {status} {s}')

s = "ssssss"
ret = sol.partitionString(s)
expect = 6
status = 'OK' if ret == expect else 'NG'
print(f'{ret} {expect} {status} {s}')

s = "hdklqkcssgxlvehva"
ret = sol.partitionString(s)
expect = 4
status = 'OK' if ret == expect else 'NG'
print(f'{ret} {expect} {status} {s}')