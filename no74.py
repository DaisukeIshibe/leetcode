def removeStars_(s: str) -> str:
	len_s:int = len(s)
	s_list:list = list(s)
	for i in range(len_s):
		c = s_list[i]
		if c == '*':
			j = i - 1
			for h in range(j, -1, -1):
				if s_list[h] != '*':
					s_list[h] = '*'
					break
	
	out_list = []
	for i in range(len_s):
		if (s_list[i] != '*'):
			out_list.append(s_list[i])
	
	out_str = ''.join(out_list)
	return out_str

def removeStars(s: str) -> str:
	return ''

# Test cases
s = "leet**cod*e"
print(f'{s} -> {removeStars(s)}')  # Expected output: "lecoe"