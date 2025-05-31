def is_same(s:str) -> bool:
	return True if len(set(list(s))) == 1 else False

def longestPalindrome(self, words: list[str]) -> int:
	# First, check if there are any words that are the same
	same_dict:dict = {}
	for _, w in enumerate(words):
		if is_same(w):
			if not w in same_dict:
				same_dict[w] = 1
			else:
				same_dict[w] += 1
	uniq_w = len(set(same_dict.keys()))
	same_count = sum([v for v in same_dict.values()])

	if same_count >= (uniq_w * 4 - 2):
		same_count *= 2
	else:
		same_count = 2

	cand_list:list = [w for w in words if (not w in same_dict)]
	cand_dict:dict = {}
	while True:
		if len(cand_list) == 0:
			break
		else:
			w = cand_list.pop(0)
			rev_w = w[::-1]
			if rev_w in cand_list:
				if not w in cand_dict:
					cand_dict[w] = 1
				else:
					cand_dict[w] += 1
				cand_list.remove(rev_w)
	
	mirror_count:int = sum(cand_dict.values())
	mirror_count *= 4 # Each pair of mirror words contributes four to the palindrome length
	total = same_count + mirror_count
	print(f'cand_list = {cand_list}, same_count = {same_count}, mirror_count = {mirror_count}, total = {total}')
	return total

w = ["lc","cl","gg"]
print(f'words = {w} act = {longestPalindrome(None, w)} expect = 6')
w = ["ab","ty","yt","lc","cl","ab"]
print(f'words = {w} act = {longestPalindrome(None, w)} expect = 8')
w = ["cc","ll","xx"]
print(f'words = {w} act = {longestPalindrome(None, w)} expect = 2')