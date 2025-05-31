def validPalindrome_(self, s: str) -> bool:	
	len_s = len(s)
	if len_s == 1:
		return True

	if s == s[::-1]:
		return True
	
	for i in range(len_s):
		s_list = list(s)
		s_list.pop(i)
		s_str = ''.join(s_list)
		if s_str == s_str[::-1]:
			return True

	return False

def validPalindrome(self, s: str) -> bool:	
	len_s = len(s)
	s_dict:dict = {}

	for i in range(len_s):
		c = s[i]
		if c in s_dict:
			s_dict[c] += 1
		else:
			s_dict[c] = 1
	
	single_list = [c for c in s_dict.values() if c == 1]
	


#s = 'abca'
#print(f's = {s} act = {validPalindrome(None, s)} expect = True')
s = 'eccer'
print(f's = {s} act = {validPalindrome(None, s)} expect = True')