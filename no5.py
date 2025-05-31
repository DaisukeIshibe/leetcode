def longestPalindrome(self, s: str) -> str:
	len_s = len(s)
	if len_s == 1:
		return s
	elif len_s == 2:
		s_list = list(s)
		if len(set(s_list)) == 1:
			return s
		else:
			return ''
	else:
		c:str = ''
		for i in range(1, len_s):
			c = s[i]
			p_flag:bool = False
			for j in range(i - 1, -1, -1):
				diff = i - j
				k = i + j + diff
				if k >= len_s:
					break
				if s[j] == s[k]:
					c = s[j] + c + s[k]
					p_flag = True
				else:
					p_flag = False
					break

			if p_flag:
				return c

		if c == '':
			for i in range(1, len_s):
				c = s[i]
				p_flag:bool = False
				for j in range(i - 1, -1, -1):
					diff = i - j
					k = i + j + diff
					if k >= len_s:
						break
					if c == s[k]:
						c = c + s[k]
						p_flag = True
					else:
						p_flag = False
						break
						
		else:
			return ''

#s = 'babad'
#print(f's = {s} act = {longestPalindrome(None, s)} expect = bab or aba')
s = 'cbbd'
print(f's = {s} act = {longestPalindrome(None, s)} expect = bb')