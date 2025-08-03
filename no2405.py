class Solution:
    def partitionString(self, s: str) -> int:
        sub_list = []
        start_idx = 0
        sub_str = ''
        len_s = len(s)
        while start_idx < len_s:
            end_idx = start_idx + 1
            sub_str = ''
            while end_idx <= len_s:
                sub_str = s[start_idx:end_idx]
                if len(set(sub_str)) == len(sub_str):
                    end_idx += 1
                    if end_idx == (len_s + 1):
                        sub_list.append(s[start_idx:end_idx])
                        sub_str = ''
                        break
                else:
                    sub_list.append(s[start_idx:end_idx - 1])
                    break
            if sub_list:
                start_idx += len(sub_list[-1])
            else:
                break
        
        if sub_str != '':
            sub_list.append(sub_str)

        return len(sub_list)


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

s = "yzubfsiypfrepcfftiov"
ret = sol.partitionString(s)
expect = 4
status = 'OK' if ret == expect else 'NG'
print(f'{ret} {expect} {status} {s}')

s = "cuieokbs"
ret = sol.partitionString(s)
expect = 1
status = 'OK' if ret == expect else 'NG'
print(f'{ret} {expect} {status} {s}')
