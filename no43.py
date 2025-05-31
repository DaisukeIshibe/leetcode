c2i_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9 }
i2c_dict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9' }

def n2i(num:str) -> int:
	len_n = len(num)
	total:int = 0
	for i in range(len_n, 0, -1):
		d = 10 ** (i - 1)
		num_int = c2i_dict[num[len_n - i]]
		total += num_int * d

	return total


def i2n(num:int) -> str:
	out_str:str = ''
	while True:
		d = num // 10
		m = num % 10
		out_str = i2c_dict[m] + out_str

		if d < 1:
			break
		else:
			num = d

	return out_str

def multiply(num1: str, num2: str) -> str:
	n1:int = n2i(num1)
	n2:int = n2i(num2)
	print(n1, n2)
	ans = i2n(n1 * n2)
	return ans

n1 = '2'
n2 = '3'
print(f'n1 = {n1} n2 = {n2} act = {multiply(n1, n2)} expect = 6')
n1 = '123'
n2 = '456'
print(f'n1 = {n1} n2 = {n2} act = {multiply(n1, n2)} expect = 56088')