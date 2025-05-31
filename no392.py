def make_dict(w: str) -> dict:
	w_dict = {}
	for i in range(len(w)):
		c = w[i]
		if not c in w_dict:
			w_dict[c] = 1
		else:
			w_dict[c] += 1

	return w_dict

def isSubsequence_(s: str, t: str) -> bool:
	s_dict = make_dict(s)
	t_dict = make_dict(t)
	
	cont_flag = False
	for k, v in s_dict.items():
		if k in t_dict:
			if v <= t_dict[k]:
				cont_flag = True
			else:
				cont_flag = False
				break
		else:
			cont_flag = False
			break

	if cont_flag:
		c_list:list = [''] * len(s)
		idx:int = 0
		for _, c in enumerate(t):
			if c in s_dict:
				if idx == len(s):
					break
				c_list[idx] = c
				idx += 1

		c_str:str = ''.join(c_list)
		print(f's = {s} t = {t} c_str = {c_str}')
		if c_str == s:
			return True
		else:
			return False
	else:
		return False

def isSubsequence(s: str, t: str) -> bool:
	len_s = len(s)
	len_t = len(t)
	match_count:int = 0
	idx_s:int = 0
	idx_t:int = 0

	while True:
		c_s = s[idx_s]
		c_t = t[idx_t]
		if c_s == c_t:
			match_count += 1
			idx_s += 1
			idx_t += 1
		else:
			idx_t += 1
		
		if idx_s == len_s or idx_t == len_t:
			break

	if match_count == len_s:
		return True
	else:
		return False

s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t)) # True
s = "acb"
t = "ahbgdc"
print(isSubsequence(s, t)) # False
s = "aza"
t = "abzba"
print(isSubsequence(s, t)) # True
s = "ab"
t = "baab"
print(isSubsequence(s, t)) # True