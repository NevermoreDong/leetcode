# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return None
        new_listnode = ListNode(-1) # 新建个链表
        new_listnode.next = head    # 把老链表接到新链表后面
        slow = new_listnode         # 慢指针指向新链表第一个
        first = new_listnode.next   # 快指针指向第二个，也就是老链表第一个
        while first and first.next:
            if first.val == first.next.val: # 如果快指针的下一个和当前这个一样
                while first.next and first.val == first.next.val:
                    first = first.next
                slow.next = first.next  # 不一样的节点接到慢指针上
                first = first.next
            else:
                slow = slow.next
                first = first.next
        return new_listnode.next