from types import List
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_dict = {f:True for f in friends}
        return [n for n in friends if n in {f:True for f in friends_dict}]