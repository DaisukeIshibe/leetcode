from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        head = reverse(head)
        carry = 0
        curr = head

        while curr:
            total = curr.val * 2 + carry
            curr.val = total % 10
            carry = total // 10

            if not curr.next and carry:
                curr.next = ListNode(carry)
                break  # 新しいノードを追加したらループを終了
            
            curr = curr.next
        
        return reverse(head)

# テスト用のヘルパー関数
def create_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    curr = head
    for num in nums[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    return head

def list_to_array(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

sol = Solution()
# [9,9,9]のテスト
test_list = create_list([9,9,9])
result = sol.doubleIt(test_list)
print(f'{list_to_array(result)} expect [1,9,9,8]')