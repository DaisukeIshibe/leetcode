class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        bin_list = [bin(a) for a in arr]
        print(bin_list)
        return

sol = Solution()
print(f'{sol.sortByBits([0,1,2,3,4,5,6,7,8])} expected [0,1,2,4,8,3,5,6,7]')
print(f'{sol.sortByBits([1024,512,256,128,64,32,16,8,4,2,1])} expect [1,2,4,8,16,32,64,128,256,512,1024]')