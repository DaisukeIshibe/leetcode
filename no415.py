c2i_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
i2c_dict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

def s2i(n:str) -> int:
	len_n = len(n)
	t:int = 0
	for i in range(len_n):
		t += (10 ** i) * c2i_dict[n[len_n - i - 1]]
	return t

def i2s(n:int) -> str:
	n_org = n
	d_count:int = 0
	while True:
		n = n // 10
		if n >= 10:
			d_count += 1
		else:
			break
	
	d_count += 1
	c_list = [''] * (d_count + 1)
	p:int = 0
	for d in range(d_count, -1, -1):
		v = 10 ** d
		a = n_org // v
		print(f'd = {d} v = {v} a = {a} d_count = {d_count} n_org = {n_org} p = {p} c_list = {c_list}')
		c_list[p] = i2c_dict[a]
		n_org = n_org - a*v
		p += 1
	return ''.join(c_list)

def addStrings(num1: str, num2: str) -> str:
	total_i = s2i(num1) + s2i(num2)
	total_s = i2s(total_i)

	return total_s

a = '9'
b = '99'
print(f'{a} + {b} = {addStrings(a, b)} expect = 108')