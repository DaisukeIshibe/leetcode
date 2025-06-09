def split_list(input_list, n):
    for idx in range(0, len(input_list), n):
        yield input_list[idx:idx + n]

def groupThePeople(self, groupSizes: list[int]) -> list:
	g_dict:dict = {}
	for idx, n in enumerate(groupSizes):
		if not n in g_dict:
			g_dict[n] = [idx]
		else:
			g_dict[n].append(idx)

	print(g_dict)
	out_list:list = []
	for k, v in g_dict.items():
		if len(v) <= k:
			out_list.append(v)
		else:
			len_v = len(v)
			div = len_v // k
			for s in split_list(v, len_v // div):
				out_list.append(s)

	return out_list


groupSizes = [3,3,3,3,3,1,3]
print(groupThePeople(None, groupSizes)) # [[5],[0,1,2],[3,4,6]]