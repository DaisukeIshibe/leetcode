from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        answer: Optional[str] = None
        path: list[str] = []

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal answer
            if not node:
                return

            path.append(chr(node.val + ord('a')))

            if not node.left and not node.right:
                candidate = ''.join(reversed(path))
                if answer is None or candidate < answer:
                    answer = candidate
            else:
                dfs(node.left)
                dfs(node.right)

            path.pop()

        dfs(root)
        return answer if answer is not None else ""