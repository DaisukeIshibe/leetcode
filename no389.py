def findTheDifference(s: str, t: str) -> str:
	if len(s) == 0:
		return t
	
	s_dict:dict = {}
	for i in range(len(s)):
		if s[i] in s_dict:
			s_dict[s[i]] += 1
		else:
			s_dict[s[i]] = 1

	t_dict:dict = {}
	for i in range(len(t)):
		if t[i] in t_dict:
			t_dict[t[i]] += 1
		else:
			t_dict[t[i]] = 1
	
	for key_t in t_dict.keys():
		if key_t in s_dict:
			t_dict[key_t] -= 1

	for k, v in t_dict.items():
		if v >= 1:
			return k
	return ''

# Test cases
print(findTheDifference("a", "aa"))  # Output: "a"