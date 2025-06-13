class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True

# Example usage:
sol = Solution()
print(sol.checkPowersOfThree(12))  # Output: True
print(sol.checkPowersOfThree(91))  # Output: True
print(sol.checkPowersOfThree(21))  # Output: False