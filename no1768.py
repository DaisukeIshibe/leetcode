def mergeAlternately(word1: str, word2: str) -> str:
	len_w1 = len(word1)
	len_w2 = len(word2)
	out_str = [''] * (len_w1 + len_w2)

	for idx in range(len_w1 + len_w2):
		new_idx1 = idx*2
		if idx >= len_w2:
			out_str[new_idx1:] = word1[idx:]
			break
		else:
			out_str[new_idx1] = word1[idx]

		new_idx2 = idx*2 + 1
		if idx >= len_w1:
			out_str[new_idx2:] = word2[idx:]
			break
		else:
			out_str[new_idx2] = word2[idx]
	
	return out_str

w1 = "abc"
#w1 = "eebeddcd"
w2 = "pqr"
#w2 = "caeeeecd"

print(mergeAlternately(w1, w2)) 