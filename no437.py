# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_count = {0: 1}
        return self.dfs(root, 0, targetSum, prefix_count)

    def dfs(
        self,
        node: Optional[TreeNode],
        current_sum: int,
        targetSum: int,
        prefix_count: dict[int, int],
    ) -> int:
        if not node:
            return 0

        current_sum += node.val
        count = prefix_count.get(current_sum - targetSum, 0)

        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
        count += self.dfs(node.left, current_sum, targetSum, prefix_count)
        count += self.dfs(node.right, current_sum, targetSum, prefix_count)
        prefix_count[current_sum] -= 1

        return count