class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        len_n = len(nums)
        if len_n < 3:
            return False
        if len_n == 3:
            if nums[0] < nums[1] < nums[2]:
                return True
            else:
                return False
        
        first = second = float('inf')
        for n in nums:
            if n < first:
                first = n
            elif n < second:
                second = n
            else:
                return True
        return False


sol = Solution()
nums0 = [1, 2, 3, 4, 5] # True
nums1 = [5, 4, 3, 2, 1] # False
nums2 = [2,1,5,0,4,6] # True
nums3 = [20,100,10,12,5,13] # True
nums4 = [6,7,1,2] # False
nums5 = [1, 2, 1, 3] # True
nums6 = [4,5,2147483647,1,2] # True
nums7 = [0,4,2,1,0,-1,-3] # False
nums8 = [2,1,5,0,3] # False
nums9 = [1,5,0,4,1,3] # True

print(f'{nums0} act = {sol.increasingTriplet(nums0)} expect = True')
print(f'{nums1} act = {sol.increasingTriplet(nums1)} expect = False')
print(f'{nums2} act = {sol.increasingTriplet(nums2)} expect = True')
print(f'{nums3} act = {sol.increasingTriplet(nums3)} expect = True')
print(f'{nums4} act = {sol.increasingTriplet(nums4)} expect = False')
print(f'{nums5} act = {sol.increasingTriplet(nums5)} expect = True')
print(f'{nums6} act = {sol.increasingTriplet(nums6)} expect = True')
print(f'{nums7} act = {sol.increasingTriplet(nums7)} expect = False')
print(f'{nums8} act = {sol.increasingTriplet(nums8)} expect = False')
print(f'{nums9} act = {sol.increasingTriplet(nums9)} expect = True')