class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -1
            else:
                count += 1
        nums.sort(reverse=True)
        for i in range(len(nums)):
            if nums[i] == -1:
                nums[i] = '_'
        print(nums)
        return count

sol = Solution()
nums = [3,2,2,3]
val = 3
print(sol.removeElement(nums, val)) # Expect 2, nums = [2,2,_,_]

nums = [0,1,2,2,3,0,4,2]
val = 2
print(sol.removeElement(nums, val)) # Expect 5, nums = [0,1,4,0,3,_,_,_]
