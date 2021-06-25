# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1: return l2
        if not l2: return l1
        
        output = ListNode()
        head = output
        
        while l1 and l2:
            if l1.val <= l2.val:
                output.next = l1
                l1 = l1.next
            else:
                output.next = l2
                l2 = l2.next
            output = output.next
        
        while l1:
            output.next = l1
            l1 = l1.next
            output = output.next

        while l2:
            output.next = l2
            l2 = l2.next
            output = output.next

        return head.next
    
    
# Method-2
# A little change

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1: return l2
        if not l2: return l1
        
        output = ListNode()
        head = output
        
        while l1 and l2:
            if l1.val <= l2.val:
                output.next = l1
                l1 = l1.next
            else:
                output.next = l2
                l2 = l2.next
            output = output.next
        
        # rather than storing remaining values
        # just point the pointer
        if l1:
            output.next = l1
            
        if l2:
            output.next = l2

        return head.next