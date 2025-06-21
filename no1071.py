def gcdOfStrings(str1: str, str2: str) -> str:
	import math
	len_str1 = len(str1)
	len_str2 = len(str2)

	gcd_num = math.gcd(len_str1, len_str2)
	str_list = []

	for i in range(gcd_num):
		c1 = str1[i]
		c2 = str2[i]
		if c1 == c2:
			str_list.append(c1)
		else:
			return ''

	match_str = ''.join(str_list)
	if match_str == '':
		return ''
	
	match_count1 = str1.count(match_str)
	match_count2 = str2.count(match_str)

	if len(match_str) == len_str1 / match_count1:
		if len(match_str) == len_str2 / match_count2:
			return match_str
		else:
			return ''
	else:
		return ''


str1 = 'ABCABC'
str2 = 'ABC'
print(f'{str1} {str2} return: {gcdOfStrings(str1, str2)}')  # Output: ABC
str1 = 'ABABAB'
str2 = 'ABAB'
print(f'{str1} {str2} return: {gcdOfStrings(str1, str2)}')  # Output: AB
str1 = 'LEET'
str2 = 'CODE'
print(f'{str1} {str2} return: {gcdOfStrings(str1, str2)}')  # Output: ''
str1 = 'ABCDEF'
str2 = 'ABC'
print(f'{str1} {str2} return: {gcdOfStrings(str1, str2)}')  # Output: ''
str1 = 'AAAAAAAAA'
str2 = 'AAACCC'
print(f'{str1} {str2} return: {gcdOfStrings(str1, str2)}')  # Output: ''
str1 = 'ABABCCABAB'
str2 = 'ABAB'
print(f'{str1} {str2} return: {gcdOfStrings(str1, str2)}')  # Output: ''