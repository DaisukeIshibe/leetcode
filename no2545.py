class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        score.sort(key=lambda x: x[k], reverse=True)
        return score

sol = Solution()
score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2
ans = [[7,5,11,2],[10,6,9,1],[4,8,3,15]]
if ans == sol.sortTheStudents(score, k):
    print('No1 OK')
else:
    print('No1 NG')


score = [[3,4],[5,6]]
k = 0
ans = [[5,6],[3,4]]
if ans == sol.sortTheStudents(score, k):
    print('No2 OK')
else:
    print('No2 NG')
