from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_linked_list(start: ListNode, end: ListNode) -> ListNode:
            prev = None
            current = start
            while current != end:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev  # 新しい先頭ノードを返す

        group_size = 1
        current = head
        prev_group_end = None

        while current:
            group_start = current
            count = 0

            # グループの終端を見つける
            while current and count < group_size:
                current = current.next
                count += 1

            if count % 2 == 0:  # グループの長さが偶数の場合、反転する
                new_group_start = reverse_linked_list(group_start, current)
                if prev_group_end:
                    prev_group_end.next = new_group_start
                else:
                    head = new_group_start  # 最初のグループの場合、headを更新
                group_start.next = current  # 反転後のグループの終端を次のグループに接続
                prev_group_end = group_start  # 次のグループの前の終端を更新
            else:
                # 奇数長グループの場合、グループの最後のノードを見つける
                temp = group_start
                for _ in range(count - 1):
                    temp = temp.next
                prev_group_end = temp

            group_size += 1

        return head

# テスト用のヘルパー関数
def create_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# テスト
sol = Solution()
test_list = create_list([5,2,6,3,9,1,7,3,8,4])
result = sol.reverseEvenLengthGroups(test_list)
print(f'{list_to_array(result)} expect [5,6,2,3,9,1,4,8,3,7]')