from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder_traversal(node: Optional[TreeNode], result: List[int]):
            if node:
                inorder_traversal(node.left, result)
                result.append(node.val)
                inorder_traversal(node.right, result)
        
        elements = []
        inorder_traversal(root1, elements)
        inorder_traversal(root2, elements)
        
        return sorted(elements)