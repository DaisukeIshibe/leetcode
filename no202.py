def isHappy(n: int) -> bool:
	while True:
		total:int = 0
		n_str:str = str(n)
		len_n:int = len(n_str)
	
		for i in range(len_n):
			c = n_str[i]
			int_c = int(c)
			total = total + int_c*int_c
		print(f'n = {n} total = {total}')

		if total == 1:
			return True
		elif total <= 4:
			return False
		else:
			n = total
	

n = 19
print(f'{n} is happy = {isHappy(n)} expect = True')
n = 2
print(f'{n} is happy = {isHappy(n)} expect = False')
n = 1111111
print(f'{n} is happy = {isHappy(n)} expect = True')