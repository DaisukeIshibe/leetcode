import itertools

def lengthOfLongestSubstring_(s: str) -> int:
	s_list = list(s)
	unq_list = list(set(s_list))
	len_unq = len(unq_list)

	for i in range(len_unq, 1, -1):
		for conb in itertools.permutations(unq_list, i):
			c_str = ''.join(conb)
			if c_str in s:
				return i

	return 1

def lengthOfLongestSubstring(s: str) -> int:
	len_s = len(s)
	max_len = len_s // 2
	list_s = list(s)

	


#s = 'abcabcbb'
#print(f's = {s} act = {lengthOfLongestSubstring(None, s)} expect = 3')
s = 'pwwkew'
print(f's = {s} act = {lengthOfLongestSubstring(None, s)} expect = 3')