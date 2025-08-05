class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        nums2_k_list = [n * k for n in nums2]
        count: int = 0
        for n1 in nums1:
            for n2 in nums2_k_list:
                if n1 % n2 == 0:
                    count += 1
        return count
    
sol = Solution()
nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1
print(f'{sol.numberOfPairs(nums1, nums2, k)} expect 5')
nums1 = [1,2,4,12]
nums2 = [2,4]
k = 3
print(f'{sol.numberOfPairs(nums1, nums2, k)} expect 2')