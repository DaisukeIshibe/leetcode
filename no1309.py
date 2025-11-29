class Solution:
    def freqAlphabets(self, s: str) -> str:
        w_dict = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i',
                  '10#':'j', '11#':'k', '12#':'l', '13#':'m', '14#':'n', '15#':'o', '16#':'p',
                  '17#':'q', '18#':'r', '19#':'s','20#':'t','21#':'u','22#':'v','23#':'w',
                  '24#':'x', '25#':'y','26#':'z'}

        print(s)
        out_list = []
        len_s = len(s)
        while len_s > 0:
            pass
        skip_flag = False
        for i in range(len(s) - 2):
            a = s[i]
            b = s[i + 1]
            c = s[i + 2]
            if c == '#':
                skip_flag = True
                sub_str = a + b + c
                print('out->', w_dict[sub_str])
            else:
                if skip_flag:
                    if a == '#':
                        skip_flag = False
                    continue
                else:
                    print(a,b,c)
        return out_list

sol = Solution()
print(f'{sol.freqAlphabets("10#11#12")} expect jkab')
print(f'{sol.freqAlphabets("1326#")} expect acz')