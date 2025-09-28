class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        n = len(points)
        max_area = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
                    max_area = max(max_area, area)
        return max_area

sol = Solution()
print(f'{sol.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]])} expect 2')
print(f'{sol.largestTriangleArea([[1,0],[0,0],[0,1]])} expect 0.5')
print(f'{sol.largestTriangleArea([[4,6],[6,5],[3,1]])} expect 5.5')