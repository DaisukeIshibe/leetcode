class Solution:
    def frequencySort(self, s: str) -> str:
        freq_dict: dict = {}
        for c in s:
            if not c in freq_dict:
                freq_dict[c] = 1
            else:
                freq_dict[c] += 1

        sorted_list = sorted(freq_dict.items(), key=lambda x:x[1], reverse=True)
        freq_dist_dict = {}
        for c, f in sorted_list:
            if not f in freq_dist_dict:
                freq_dist_dict[f] = [c]
            else:
                freq_dist_dict[f].append(c)
        for k in freq_dist_dict.keys():
            freq_dist_dict[k] = sorted(freq_dist_dict[k])

        out_list = []
        for k, v_list in freq_dist_dict.items():
            for v in v_list:
                out_list.extend([v] * k)
        
        return ''.join(out_list)

sol = Solution()
print(f'{sol.frequencySort("tree")} expect eert')
print(f'{sol.frequencySort("cccaaa")} expect aaaccc')
print(f'{sol.frequencySort("Aabb")} expect bbAa')
