class Solution:
    def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        cat_list = ['electronics','grocery','pharmacy','restaurant']
        cat_set = {c for c in cat_list}
        dst_dict = {c:[] for c in cat_list}
        for c, b, i in zip(code, businessLine, isActive):
            if not i:
                continue
            if b.lower() not in cat_set:
                continue
            if c == '':
                continue
            if ('@' in c) or ('-' in c) or ("'" in c) or ('/' in c) or ('"' in c):
                continue
            dst_dict[b].append(c)
            
        for k in dst_dict.keys():
            dst_dict[k].sort()
        out_list = []
        for c in cat_list:
            out_list.extend(dst_dict[c])
        return out_list

sol = Solution()
print(f'{sol.validateCoupons(
    ["SAVE20","","PHARMA5","SAVE@20"],
    ["restaurant","grocery","pharmacy","restaurant"],
    [True,True,True,True])} expect ["PHARMA5","SAVE20"]')
print(f'{sol.validateCoupons(
    ["GROCERY15","ELECTRONICS_50","DISCOUNT10"],
    ["grocery","electronics","invalid"],
    [False,True,True])} expect ["ELECTRONICS_50"]')
print(f'{sol.validateCoupons(
    ["1OFw","0MvB"],
    ["electronics","pharmacy"],
    [True,True])} expect ["1OFw","0MvB"]')
print(f'{sol.validateCoupons(["pBXoMqBU0_aMgc9F8dy6TaSzza3KjSJFjxZa_NuyMjzEBR7fJNwpGHh7lzuoZvQeEUeo6YumHmIOjjchXlzSVa4ItdyDOImQgm","P8rIIUl35MW8yrqRbO0N_IITptYOxz9tOCbPL6d1aIF_hM2sapaDtUzNpmAZRmJQB1WgjLh8bdYADuSRSU21OzttUkq73qiA66","aFWkYookQlHYMXzhVGxbnrXIl1810ws3qHtketHSECHqJoktWXVZGc6ZyeOuzA_VL9zFL9znpIHwbkwJF2bOPQqsz3_0PYgETJ"],
                             ["pharmacy","invalid","pharmacy"],
                             [True,True,True])} expect ["aFWkYookQlHYMXzhVGxbnrXIl1810ws3qHtketHSECHqJoktWXVZGc6ZyeOuzA_VL9zFL9znpIHwbkwJF2bOPQqsz3_0PYgETJ","pBXoMqBU0_aMgc9F8dy6TaSzza3KjSJFjxZa_NuyMjzEBR7fJNwpGHh7lzuoZvQeEUeo6YumHmIOjjchXlzSVa4ItdyDOImQgm"]')