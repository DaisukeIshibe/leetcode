def validPalindrome(self, s: str) -> bool:
	len_s = len(s)
	half_len = len_s // 2
	
	s1_list = list(s)
	s2_list = list(s)
	for i in range(half_len):
		head = s[i]
		tail = s[-(i + 1)]
		if head != tail:
			s1_list.pop(i)
			s1 = ''.join(s1_list)
			if s1[::-1] == s1:
				return True
			s2_list.pop(-(i + 1))
			s2 = ''.join(s2_list)
			if s2[::-1] == s2:
				return True
			return False

	return True
	

s = 'aba'
print(f's = {s} act = {validPalindrome(None, s)} expect = True')
s = 'abca'
print(f's = {s} act = {validPalindrome(None, s)} expect = True')
s = 'abc'
print(f's = {s} act = {validPalindrome(None, s)} expect = False')
s = 'eccer'
print(f's = {s} act = {validPalindrome(None, s)} expect = True')
s = 'deeee'
print(f's = {s} act = {validPalindrome(None, s)} expect = True')