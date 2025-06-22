def countLargestGroup(n: int) -> int:
	import collections
	hashMap = collections.Counter()
	for i in range(1, n + 1):
		key = sum([int(x) for x in str(i)])
		hashMap[key] += 1
	maxValue = max(hashMap.values())
	count = sum(1 for v in hashMap.values() if v == maxValue)
	#print(hashMap)
	return count

def countLargestGroup_(n: int) -> int:
	if n < 10:
		return 1

	sum_dict: dict = {}
	for i in range(1, n + 1):
		if i < 10:
			continue
		sum_digit = calcSum(i)

		used_dict: dict = {}
		if not sum_digit in sum_dict:
			if not sum_digit in used_dict:
				sum_dict[sum_digit] = [i]
				used_dict[i] = True
		else:
			sum_dict[sum_digit].append(i)

	len_num_list = [len(v)+1 for v in sum_dict.values()]
	count_dict: dict = {}
	for n in len_num_list:
		if not n in count_dict:
			count_dict[n] = 1
		else:
			count_dict[n] += 1
	#print('sum_dict', sum_dict)
	#print('len_num_list', len_num_list)
	#print('not chosen_dict', not_chosen_dict.keys())
	return max(count_dict.values())

def calcSum(n: int) -> int:
	n_str = str(n)
	n_len = len(n_str)
	total: int = 0
	for i in range(n_len):
		total += int(n_str[i])
	
	return total

print(f"13, {countLargestGroup(13)} Expect 4")
print(f"24, {countLargestGroup(24)} Expect 5")
print(f"46, {countLargestGroup(46)} Expect 6")
print(f"264, {countLargestGroup(264)} Expect 2")
print(f"33, {countLargestGroup(33)} Expect 4")