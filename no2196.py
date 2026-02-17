from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        
        for parent, child, is_left in descriptions:
            parent_node = nodes.setdefault(parent, TreeNode(parent))
            child_node = nodes.setdefault(child, TreeNode(child))
            
            if is_left:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            
            children.add(child)
        
        # ルートノードを見つける（子として登場しないノード）
        for val in nodes:
            if val not in children:
                return nodes[val]