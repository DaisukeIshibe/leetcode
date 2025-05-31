def isPowerOfThree(self, n: int) -> bool:
	i = n
	for _ in range(n//4):
		j = (i + 1) // 2
		p3 = j ** 3
		if p3 == n:
			return True
		elif p3 > n:
			i = j
		else:
			i += 2
		
	return False

n = 27
print(f'n = {n} act = {isPowerOfThree(None, n)} expect = True')