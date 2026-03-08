from typing import Optional, List
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        count = defaultdict(int)

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            total_sum = node.val + left_sum + right_sum
            count[total_sum] += 1
            return total_sum

        dfs(root)

        max_freq = max(count.values())
        return [s for s, freq in count.items() if freq == max_freq]