from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        if n == 0:
            return []
        
        def generate_trees(start: int, end: int) -> list[Optional[TreeNode]]:
            if start > end:
                return [None]
            
            all_trees = []
            for i in range(start, end + 1):
                # Generate all left and right subtrees
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)
                
                # Combine left and right subtrees with the current root node
                for left in left_trees:
                    for right in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = left
                        current_tree.right = right
                        all_trees.append(current_tree)
            
            return all_trees
        
        return generate_trees(1, n)