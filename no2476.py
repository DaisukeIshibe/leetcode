from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        arr = []
        dfs(root)
        res = []
        for q in queries:
            idx = bisect.bisect_left(arr, q)
            if idx == len(arr):
                res.append([arr[-1], -1])
            elif arr[idx] == q:
                res.append([q, q])
            elif idx == 0:
                res.append([-1, arr[0]])
            else:
                res.append([arr[idx - 1], arr[idx]])
        return res