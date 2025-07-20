class Solution:
    def findCommonResponse(self, responses: list[list[str]]) -> str:
        dst_list: list = []
        for res in responses:
            dst_list.extend(list(set(res)))
        d_dict: dict = {}
        for a in dst_list:
            if not a in d_dict:
                d_dict[a] = 1
            else:
                d_dict[a] += 1
        
        max_v = sorted(d_dict.values())[-1]
        key_list = [k for k, v in d_dict.items() if v == max_v]
        return sorted(key_list)[0]


sol = Solution()
responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]
print(f'{sol.findCommonResponse(responses)} expect good')
responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]
print(f'{sol.findCommonResponse(responses)} expect bad')