class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        common_list = list(set({n for n in nums1}) & set({n for n in nums2}))
        
        if common_list == []:
            return [0, 0]
        else:
            nums1_count = 0
            for i in nums1:
                if i in common_list:
                    nums1_count += 1
            nums2_count = 0
            for i in nums2:
                if i in common_list:
                    nums2_count += 1
            return [nums1_count, nums2_count]


sol = Solution()
print(f'{sol.findIntersectionValues([2,3,2], [1,2])} expect [2, 1]')
print(f'{sol.findIntersectionValues([4,3,2,3,1], [2,2,5,2,3,6])} expect [3, 4]')
print(f'{sol.findIntersectionValues([3,4,2,3], [1,5])} expect [0, 0]')