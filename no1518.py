class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        while numBottles != 0:
            mod = numBottles % numExchange
            numBottles += mod
            print(f'{numBottles}')
            numBottles //= numExchange
            count += numBottles
        return count

sol = Solution()
print(f'{sol.numWaterBottles(9, 3)} expect 13')
print(f'{sol.numWaterBottles(15, 4)} expect 19')