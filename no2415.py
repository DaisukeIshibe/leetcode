from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        from collections import deque
        
        queue = deque([root])
        level = 0
        
        while queue:
            level_size = len(queue)
            current_level_nodes = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level_nodes.append(node)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level % 2 == 1:
                values = [node.val for node in current_level_nodes][::-1]
                for i, node in enumerate(current_level_nodes):
                    node.val = values[i]
            
            level += 1
        
        return root