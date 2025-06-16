from collections import OrderedDict

def encode(word) -> list:
	w_dict = OrderedDict()
	count = 0
	for c in word:
		if not c in w_dict:
			w_dict[c] = count
			count += 1
	
	w_dict = {k:v for k, v in w_dict.items()}
	out_list = []
	for w in word:
		out_list.append(str(w_dict[w]))
	return out_list


def findAndReplacePattern(words: list[str], pattern: str) -> list[str]:
	encode_pattern = encode(pattern)
	#print(encode_pattern)
	out_list = []
	for w in words:
		encode_w = encode(w)
		if encode_w == encode_pattern:
			out_list.append(w)
	
	return out_list

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
print(findAndReplacePattern(words, pattern))

words = ["a","b","c"]
pattern = "a"
print(findAndReplacePattern(words, pattern))

words = ["badc","abab","dddd","dede","yyxx"]
pattern = "baba"
print(findAndReplacePattern(words, pattern)) # "abab" "dede"

words =  ["abcdefghijkba"]
pattern = "qwertyuiopwqa"
print(findAndReplacePattern(words, pattern)) # ""
