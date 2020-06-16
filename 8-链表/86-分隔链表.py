# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        point_1 = dummy1 # 设置指针
        point_2 = dummy2

        while head:
            if head.val < x:
                point_1.next = head
                point_1 = point_1.next
            else:
                point_2.next = head
                point_2 = point_2.next
            head = head.next
        point_1.next = dummy2.next
        point_2.next = None  # 必须要有的
        return dummy1.next