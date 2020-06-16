# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:


        tmp_list = []
        point = head
        while point is not None:
            tmp_list.append(point.val)
            point = point.next
        r_list = tmp_list[m-1:n]
        r_list.reverse()
        ans_list = tmp_list[:m-1] + r_list + tmp_list[n:len(tmp_list)]
        dummpy = ListNode(-1)
        pt = dummpy
        for i in ans_list:
            pt.next = ListNode(i)
            pt = pt.next
        return dummpy.next