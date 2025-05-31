def reverseWords(s: str) -> str:
	s_list = s.split()[::-1]
	return ' '.join(s_list)

s = "the sky is blue"
print(reverseWords(s))  # Output: "blue is sky the"