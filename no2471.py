from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        from collections import deque
        queue = deque([root])
        ans = 0

        while queue:
            size = len(queue)
            arr = []

            for _ in range(size):
                node = queue.popleft()
                arr.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            sorted_arr = sorted(arr)
            index_map = {v: i for i, v in enumerate(sorted_arr)}
            visited = [False] * size

            for i in range(size):
                if visited[i] or index_map[arr[i]] == i:
                    continue

                cycle_size = 0
                j = i

                while not visited[j]:
                    visited[j] = True
                    j = index_map[arr[j]]
                    cycle_size += 1

                if cycle_size > 0:
                    ans += (cycle_size - 1)

        return ans