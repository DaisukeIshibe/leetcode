class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        for f in fruits:
            for idx, b in enumerate(baskets):
                if f <= b:
                    baskets[idx] = -1
                    break
        
        count = 0
        for b in baskets:
            if b != -1:
                count += 1
        return count

sol = Solution()
fruits = [4,2,5]
baskets = [3,5,4]
print(f'{sol.numOfUnplacedFruits(fruits, baskets)} expect 1')
fruits = [3,6,1]
baskets = [6,4,7]
print(f'{sol.numOfUnplacedFruits(fruits, baskets)} expect 0')