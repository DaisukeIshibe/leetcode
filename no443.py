class Solution:
    def compress(self, chars: list[str]) -> int:
        char_list = []
        for c in chars:
            if char_list == []:
                char_list.append([c])
            else:
                if char_list[-1][-1] == c:
                    char_list[-1].append(c)
                else:
                    char_list.append([c])

        count_list = [[c[0], c.count(c[0])] for c in char_list]
        out_list = []
        for char, count in count_list:
            if count == 1:
                out_list.append(char)
            else:
                count_str = str(count)
                out_list.append(char)
                for c in count_str:
                    out_list.append(c)

        print(out_list)
        return len(out_list)

sol = Solution()
print(f'{sol.compress(["a","a","b","b","c","c","c"])} expect 6 / "a2b2c3"')
print(f'{sol.compress(["a"])} expect 1 / "a"')
print(f'{sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])} expect 4 / "["a","b","1","2"]"')
print(f'{sol.compress(["a","a","a","b","b","a","a"])}, expect 6 / "["a","3","b","2","a","2"]"')