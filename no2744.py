class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        w_list = [''.join(sorted(w)) for w in words]
        w_dict = {}
        for w in w_list:
            if not w in w_dict:
                w_dict[w] = 1
            else:
                w_dict[w] += 1

        count = 0
        for _, v in w_dict.items():
            if v >= 2:
                count += 1
        return count

sol = Solution()
print(f'{sol.maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"])} expect 2')
print(f'{sol.maximumNumberOfStringPairs(["ab","ba","cc"])} expect 2')
print(f'{sol.maximumNumberOfStringPairs(["aa","ab"])} expect 0')