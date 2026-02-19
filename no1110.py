from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        
        to_delete_set = set(to_delete)
        result: List[TreeNode] = []
        append_result = result.append

        stack = [(root, None, False, True)]

        while stack:
            node, parent, is_left_child, is_root = stack.pop()
            if not node:
                continue

            deleted = node.val in to_delete_set

            if deleted and parent:
                if is_left_child:
                    parent.left = None
                else:
                    parent.right = None
            elif is_root:
                append_result(node)

            child_is_root = deleted
            stack.append((node.right, node, False, child_is_root))
            stack.append((node.left, node, True, child_is_root))

        return result