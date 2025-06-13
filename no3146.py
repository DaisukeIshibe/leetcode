def makeDict(s: str) -> dict:
	out_dict:dict = {}
	for idx, c in enumerate(s):
		out_dict[c] = idx
	
	return out_dict


def findPermutationDifference(self, s: str, t: str) -> int:
	s_dict = makeDict(s)
	t_dict = makeDict(t)
	print(s_dict)
	print(t_dict)

	total:int = 0
	for k_s, v_s in s_dict.items():
		v_t = t_dict.get(k_s, -1)
		total += abs(v_s - v_t)

	return total

print(findPermutationDifference(None, "abc", "bac"))  # Output: 2
print(findPermutationDifference(None, "abcde", "edbac"))  # Output: 12