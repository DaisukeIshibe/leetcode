class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        h = len(score)
        target_list = []
        for i in range(h):
            target_list.append(score[i][k])
        sorted_list = sorted(target_list, reverse=True)
        print(f'target {target_list} {sorted_list}')
        return

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
