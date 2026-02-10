from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder_traversal(node: Optional[TreeNode], nodes: List[TreeNode]) -> None:
            if not node:
                return
            inorder_traversal(node.left, nodes)
            nodes.append(node)
            inorder_traversal(node.right, nodes)

        def build_balanced_bst(nodes: List[TreeNode], left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            root = nodes[mid]
            root.left = build_balanced_bst(nodes, left, mid - 1)
            root.right = build_balanced_bst(nodes, mid + 1, right)
            return root

        nodes = []
        inorder_traversal(root, nodes)
        return build_balanced_bst(nodes, 0, len(nodes) - 1)