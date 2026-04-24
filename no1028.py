# We run a preorder depth-first search (DFS) on the root of a binary tree.
# At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.
# If a node has only one child, that child is guaranteed to be the left child.
# Given the output traversal of this traversal, recover the tree and return its root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        while i < len(traversal):
            level = 0
            while i < len(traversal) and traversal[i] == '-':
                level += 1
                i += 1
            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            node = TreeNode(value)
            if level == len(stack):
                if stack:
                    stack[-1].left = node
            else:
                while level != len(stack):
                    stack.pop()
                stack[-1].right = node
            stack.append(node)
        return stack[0] if stack else None