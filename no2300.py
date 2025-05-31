def successfulPairs_(spells: list[int], potions: list[int], success: int) -> list[int]:
	out_list:list = []
	for s in spells:
		p_list = [p * s for p in potions]
		sucess_num = len([p for p in p_list if p >= success])
		print(f's = {s} p_list = {p_list} sucess_num = {sucess_num}')
		out_list.append(sucess_num)
	return out_list

def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
	out_list:list = []
	for s in spells:
		p_list = [True for p in potions if p * s >= success]
		print(f's = {s} p_list = {p_list}')
		out_list.append(len(p_list))
	return out_list

spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
sucess = 7
print(f'spells = {spells} potions = {potions} sucess = {sucess} act = {successfulPairs(spells, potions, sucess)} expect = [4, 0, 3]')