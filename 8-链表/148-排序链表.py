# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        point_1 = head
        node_list = []
        while point_1:
            node_list.append(point_1.val)
            point_1 = point_1.next
        node_list.sort()

        link_list = ListNode(-1)
        point_2 = link_list
        for i in node_list:
            point_2.next = ListNode(i)
            point_2 = point_2.next
        return link_list.next