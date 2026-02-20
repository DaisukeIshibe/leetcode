from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = [(root, 0)]
        max_depth = 0
        deepest_leaves = []

        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                if depth > max_depth:
                    max_depth = depth
                    deepest_leaves = [node]
                elif depth == max_depth:
                    deepest_leaves.append(node)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        def find_lca(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node or node in deepest_leaves:
                return node
            
            left_lca = find_lca(node.left)
            right_lca = find_lca(node.right)

            if left_lca and right_lca:
                return node
            return left_lca or right_lca

        return find_lca(root)