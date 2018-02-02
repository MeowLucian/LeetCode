# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        flag = head
        while flag:
            point = flag.next
            while point and point.val == flag.val:
                point = point.next
            flag.next = point
            flag = point
       
        return head