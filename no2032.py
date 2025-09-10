class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        import collections
        
        num1_dict = collections.Counter(nums1)
        num2_dict = collections.Counter(nums2)
        num3_dict = collections.Counter(nums3)
        print(num1_dict, num2_dict, num3_dict)
        return list()

sol = Solution()
print(f'{sol.twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3])} expect [3, 2]')
print(f'{sol.twoOutOfThree(nums1 = [3,1], nums2 = [2,3], nums3 = [1,2])} expect [2,3,1]')
print(f'{sol.twoOutOfThree(nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5])} expect []')