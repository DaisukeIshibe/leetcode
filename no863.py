from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        graph = {}
        self.buildGraph(root, None, graph)

        visited = set()
        queue = [(target.val, 0)]
        visited.add(target.val)
        result = []

        while queue:
            node_val, distance = queue.pop(0)

            if distance == k:
                result.append(node_val)

            for neighbor in graph.get(node_val, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))

        return result

    def buildGraph(self, node: TreeNode, parent: TreeNode, graph: dict):
        if not node:
            return

        if parent:
            graph.setdefault(node.val, []).append(parent.val)
            graph.setdefault(parent.val, []).append(node.val)

        self.buildGraph(node.left, node, graph)
        self.buildGraph(node.right, node, graph)