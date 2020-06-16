# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = head
        temp = []
        while cur:
            temp.append(cur.val)
            cur = cur.next
        temp.sort()
        res = ListNode(0)
        point = res
        for i in temp:
            point.next = ListNode(i)
            point = point.next
        return res.next