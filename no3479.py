def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
	# 修正版: ソート + 貪欲法アプローチ O(n^2) だが正確
	# 果物を小さい順にソート、バスケットを小さい順にソート
	fruits_sorted = sorted(fruits)  # 小さい順
	baskets_sorted = sorted(baskets)  # 小さい順
	
	used_baskets = [False] * len(baskets_sorted)  # バスケットの使用状況を追跡
	placed_fruits = 0
	
	# 各果物に対して、使用可能な最小のバスケットを探す
	for fruit in fruits_sorted:
		for i, basket_size in enumerate(baskets_sorted):
			if not used_baskets[i] and basket_size >= fruit:
				used_baskets[i] = True
				placed_fruits += 1
				break
	
	return len(fruits) - placed_fruits


def numOfUnplacedFruits_optimal(self, fruits: list[int], baskets: list[int]) -> int:
	# 最適解: 二分マッチング問題として解決
	# 果物を小さい順、バスケットを小さい順にソートして貪欲に割り当て
	fruits_sorted = sorted(fruits)
	baskets_sorted = sorted(baskets)
	
	used_baskets = [False] * len(baskets_sorted)
	placed_fruits = 0
	
	# 各果物に対して、使用可能な最小のバスケットを探す
	for fruit in fruits_sorted:
		for i, basket_size in enumerate(baskets_sorted):
			if not used_baskets[i] and basket_size >= fruit:
				used_baskets[i] = True
				placed_fruits += 1
				break
	
	return len(fruits) - placed_fruits


def numOfUnplacedFruits_heap(self, fruits: list[int], baskets: list[int]) -> int:
	# 最適化案2: ヒープを使用したアプローチ O(n log m)
	import heapq
	
	# バスケットを最小ヒープに変換
	available_baskets = baskets[:]
	heapq.heapify(available_baskets)
	
	placed_fruits = 0
	
	# 果物をソートして小さいものから処理
	for fruit in sorted(fruits):
		# 果物が入る最小のバスケットを探す
		temp_removed = []
		found = False
		
		while available_baskets and not found:
			smallest_basket = heapq.heappop(available_baskets)
			if smallest_basket >= fruit:
				placed_fruits += 1
				found = True
				# このバスケットは使用済みなので戻さない
			else:
				temp_removed.append(smallest_basket)
		
		# 使用できなかったバスケットを戻す
		for basket in temp_removed:
			heapq.heappush(available_baskets, basket)
	
	return len(fruits) - placed_fruits


def numOfUnplacedFruits_original(self, fruits: list[int], baskets: list[int]) -> int:
	# 元のコード（比較用）
	baskets_copy = baskets[:]  # 元の配列を保護
	count_f = 0
	for f in fruits:
		for idx, b in enumerate(baskets_copy):
			if b != -1 and f <= b:
				count_f += 1
				baskets_copy[idx] = -1
				break
	
	return len(fruits) - count_f


# テスト関数
def test_performance():
	import time
	
	# テストケース1: 元の例
	fruits1 = [3, 7, 6, 5, 8, 10, 11]
	baskets1 = [4, 7, 9, 10, 3]
	
	# テストケース2: 問題のケース
	fruits2 = [4, 2, 5]
	baskets2 = [3, 5, 4]
	
	print("=== テストケース1 ===")
	print(f"fruits: {fruits1}")
	print(f"baskets: {baskets1}")
	
	result1_orig = numOfUnplacedFruits_original(None, fruits1[:], baskets1[:])
	result1_new = numOfUnplacedFruits(None, fruits1[:], baskets1[:])
	result1_opt = numOfUnplacedFruits_optimal(None, fruits1[:], baskets1[:])
	result1_heap = numOfUnplacedFruits_heap(None, fruits1[:], baskets1[:])
	
	print(f"元のアルゴリズム: {result1_orig}")
	print(f"修正版: {result1_new}")
	print(f"最適解: {result1_opt}")
	print(f"ヒープ版: {result1_heap}")
	
	print("\n=== テストケース2 (問題のケース) ===")
	print(f"fruits: {fruits2}")
	print(f"baskets: {baskets2}")
	print("期待値: 1")
	
	result2_orig = numOfUnplacedFruits_original(None, fruits2[:], baskets2[:])
	result2_new = numOfUnplacedFruits(None, fruits2[:], baskets2[:])
	result2_opt = numOfUnplacedFruits_optimal(None, fruits2[:], baskets2[:])
	result2_heap = numOfUnplacedFruits_heap(None, fruits2[:], baskets2[:])
	
	print(f"元のアルゴリズム: {result2_orig}")
	print(f"修正版: {result2_new}")
	print(f"最適解: {result2_opt}")
	print(f"ヒープ版: {result2_heap}")
	
	# パフォーマンステスト
	print("\n=== パフォーマンステスト ===")
	test_fruits = fruits1 * 100  # 大きなデータセット
	test_baskets = baskets1 * 100
	
	start = time.time()
	numOfUnplacedFruits_original(None, test_fruits[:], test_baskets[:])
	time1 = time.time() - start
	
	start = time.time()
	numOfUnplacedFruits(None, test_fruits[:], test_baskets[:])
	time2 = time.time() - start
	
	start = time.time()
	numOfUnplacedFruits_optimal(None, test_fruits[:], test_baskets[:])
	time3 = time.time() - start
	
	print(f"元のアルゴリズム: {time1:.6f}秒")
	print(f"修正版: {time2:.6f}秒")
	print(f"最適解: {time3:.6f}秒")


if __name__ == "__main__":
	test_performance()