import string
a2n_dict = {(idx+1):s for idx, s in enumerate(string.ascii_uppercase)}

def convertToTitle(columnNumber: int) -> str:
	out_list:list = []
	a = columnNumber
	count_div:int = 0
	out_list:list = []
	while True:
		b = a // 26
		if b >= 1:
			count_div += 1 
			a = b
		else:
			break

	print(f'count_div = {count_div}')
	return ''.join(out_list)

c = 28
print(f'{c} act = {convertToTitle(c)} expect = AB')
c = 676
print(f'{c} act = {convertToTitle(c)} expect = ZZ')