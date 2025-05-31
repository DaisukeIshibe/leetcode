def removeStars_(self, s: str) -> str:
	ast_idx_dict:dict = {}
	len_s = len(s)
	for i in range(len_s):
		if s[i] == '*':
			ast_idx_dict[i] = True

	s_list = list(s)
	for i in sorted(ast_idx_dict.keys()):
		t = i - 1
		while True:
			if s_list[t] != '*':
				if s_list[t] == '-':
					t -= 1
				else:
					s_list[i] = '-'
					s_list[t] = '-'
					break
			else:
				t -= 1
	
	out_str:str = ''
	for s in s_list:
		if s != '-':
			out_str += s

	return out_str

def removeStars(self, s: str) -> str:
	asta_idx_list:list = []
	len_s = len(s)
	i:int = 0

	while i < len_s:
		if s[i] == '*':
			j:int = i
			asta_count:int = 0
			while j < len_s:
				if s[j] == '*':
					asta_count += 1
					if j == len_s - 1:
						asta_idx_list.append([i, asta_count])
						i = j
						break
					j += 1

				else:
					asta_idx_list.append([i, asta_count])
					i = j
					break
		
		i += 1

	s_list = list(s)
	print(s_list)
	print(asta_idx_list)
	for a in asta_idx_list:
		start_idx:int = a[0] - a[1]
		end_idx:int = start_idx + a[1]
		print(f'start_idx = {start_idx} end_idx = {end_idx}')
		for i in range(start_idx, end_idx):
			s_list[i] = '*'

	print(s_list)
	out_str = ''.join(s_list).replace('*', '')
	return out_str

s = 'leet**cod*e'
print(f's = {s} act = {removeStars(None, s)} expect = lecoe')
s = 'erase*****'
print(f's = {s} act = {removeStars(None, s)} expect = ')
s = 'b*'
print(f's = {s} act = {removeStars(None, s)} expect = ')
s = 'abb*cdfg*****x*'
print(f's = {s} act = {removeStars(None, s)} expect = a')