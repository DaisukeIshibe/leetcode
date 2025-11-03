# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            
            good_count = 0
            if node.val >= max_val:
                good_count = 1
                max_val = node.val
            
            good_count += dfs(node.left, max_val)
            good_count += dfs(node.right, max_val)
            
            return good_count
        
        return dfs(root, float('-inf'))