class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        mat_dict = {}
        for s in strs:
            for idx, c in enumerate(s):
                if not idx in mat_dict:
                    mat_dict[idx] = [c]
                else:
                    mat_dict[idx].append(c)

        wrong_num: int = 0
        for v in mat_dict.values():
            sorted_v = sorted(v)
            if v != sorted_v:
                wrong_num += 1
            #print(v, sorted_v)
        return wrong_num

sol = Solution()
print(f'{sol.minDeletionSize(["abc", "bce", "cae"])} expect 1')
print(f'{sol.minDeletionSize(["cba","daf","ghi"])} expect 1')
print(f'{sol.minDeletionSize(["a","b"])} expect 0')
print(f'{sol.minDeletionSize(["zyx","wvu","tsr"])} expect 3')
