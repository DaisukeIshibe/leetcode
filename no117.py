"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        leftmost = root

        while leftmost:
            # 次のレベルの最初のノードを見つける
            next_leftmost = None
            head = leftmost

            while head:
                # 左の子が存在する場合
                if head.left:
                    if not next_leftmost:
                        next_leftmost = head.left
                    if head.right:
                        head.left.next = head.right
                
                # 右の子が存在する場合
                if head.right:
                    if not next_leftmost:
                        next_leftmost = head.right
                
                # 次のノードの子と接続
                if head.next:
                    # 現在のノードの右の子と次のノードの最初の子を接続
                    if head.right:
                        head.right.next = self.getNextChild(head.next)
                    elif head.left:
                        head.left.next = self.getNextChild(head.next)

                head = head.next

            leftmost = next_leftmost

        return root
    
    def getNextChild(self, node):
        """次のノードの最初の子を取得"""
        while node:
            if node.left:
                return node.left
            if node.right:
                return node.right
            node = node.next
        return None