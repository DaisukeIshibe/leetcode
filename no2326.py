from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Create the matrix
        matrix = [[0] * n for _ in range(m)]
        # Define the boundaries of the spiral
        top, bottom, left, right = 0, m - 1, 0, n - 1
        # Fill the matrix in a spiral order
        while top <= bottom and left <= right:
            # Fill the top row
            for col in range(left, right + 1):
                if head:
                    matrix[top][col] = head.val
                    head = head.next
            top += 1
            # Fill the right column
            for row in range(top, bottom + 1):
                if head:
                    matrix[row][right] = head.val
                    head = head.next
            right -= 1
            # Fill the bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    if head:
                        matrix[bottom][col] = head.val
                        head = head.next
                bottom -= 1
            # Fill the left column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    if head:
                        matrix[row][left] = head.val
                        head = head.next
                left += 1
        return matrix