from typing import Optional
# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.
# Note that you need to maximize the answer before taking the mod and not after taking it.
# Definition for a binary tree node.

# Input: root = [1,2,3,4,5,6]
#Output: 110
#Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)]
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        MOD = 10**9 + 7
        total_sum = 0
        subtree_sums = []
        def compute_subtree_sums(node):
            # 部分木の和を計算してリストに追加する（total_sum はここでは直接更新しない）
            if not node:
                return 0
            left_sum = compute_subtree_sums(node.left)
            right_sum = compute_subtree_sums(node.right)
            subtree_sum = node.val + left_sum + right_sum
            subtree_sums.append(subtree_sum)
            return subtree_sum

        # 全体の和は根の部分木和（compute_subtree_sums の返り値）で得られる
        total_sum = compute_subtree_sums(root)
        # 各切断で生じる2つの部分木の和の積の最大値を求める
        max_prod = 0
        for s in subtree_sums:
            prod = s * (total_sum - s)
            if prod > max_prod:
                max_prod = prod
        return max_prod % MOD