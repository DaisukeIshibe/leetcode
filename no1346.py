def checkIfExist(arr:list) -> bool:
	arr_dict = {}
	#odd_list = []

	for idx, i in enumerate(arr):
		arr_dict[i] = idx
		#odd_list.append(i % 2)

	#if sum(odd_list) == len(arr):
	#    return False

	for idx, i in enumerate(arr):
		if i % 2 != 0:
			continue
		t = i // 2
		if t in arr_dict:
			if idx == arr_dict[t]:
				continue
			else:
				print(f"i: {i}, t: {t}, arr_dict[t]: {arr_dict[t]} {arr}")
				return True
	return False

check_list = [-2,0,10,-19,4,6,-8]

status = checkIfExist(check_list)
print(status)

