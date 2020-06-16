# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 快慢指针能相遇，说明存在环
        visited = set()
        cur = head
        while cur:
            if cur in visited:
                return True
            else:
                visited.add(cur)
                cur = cur.next
        return False