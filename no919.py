from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:
    import collections

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.deque = self.collections.deque()
        if root:
            queue = self.collections.deque([root])
            while queue:
                node = queue.popleft()
                if not node.left or not node.right:
                    self.deque.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    def insert(self, val: int) -> int:
        node = TreeNode(val)
        parent = self.deque[0]
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
            self.deque.popleft()
        self.deque.append(node)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()