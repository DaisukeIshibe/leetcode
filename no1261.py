from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.values = set()  # 値を保存するセット
        
        if self.root:
            self.root.val = 0
            self.values.add(0)  # ルートの値を追加
            stack = [self.root]
            while stack:
                node = stack.pop()
                if node.left:
                    node.left.val = 2 * node.val + 1
                    self.values.add(node.left.val)  # 左の子の値を追加
                    stack.append(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    self.values.add(node.right.val)  # 右の子の値を追加
                    stack.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.values  # O(1)の検索