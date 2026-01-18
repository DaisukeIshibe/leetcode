# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        
        stack = [(original, cloned)]
        
        while stack:
            orig_node, clone_node = stack.pop()
            
            if orig_node is target:
                return clone_node
            
            if orig_node.right:
                stack.append((orig_node.right, clone_node.right))
            if orig_node.left:
                stack.append((orig_node.left, clone_node.left))
        
        return None