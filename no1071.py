import re

def obtainRep(in_str: str, d:str='a') -> str:
	len_str = len(in_str)
	print(f'code:{d} len_str: {len_str}')
	
	for i in range(1, len_str):
		b = in_str[0:i]
		match_list = re.findall(b, in_str)
		print(f'code:{d} match_list: {match_list} a:{in_str} b:{b}')
		if len(match_list) * len(b) == len_str:
			return b
	return in_str

def gcdOfStrings(str1: str, str2: str) -> str:
	a = obtainRep(str1, '1')
	b = obtainRep(str2, '2')

	print(f'a:{a} b:{b}')
	if a == b:
		return a
	else:
		return ''

str1 = 'ABCABC'
str2 = 'ABC'
print(f'{str1} {str2} return: {gcdOfStrings(str1, str2)}')  # Output: ABC