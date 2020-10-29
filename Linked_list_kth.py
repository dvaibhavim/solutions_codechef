# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 11:22:55 2020
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

@author: lenovo
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy
        
        while fast.next:
            fast = fast.next
            n -= 1
            
            if n < 0:
                slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next
        '''
        ptr1 = head
        ptr2=head
        if head==None:
            return 0
        #while(ptr1!=n+1 and ptr1.next!=None):
        for _ in range(n):
            if ptr1 == None:
                return None
            ptr1 = ptr1.next
        if ptr1 == None:
             return None
        while ptr1.next!=None:
            ptr2=ptr2.next
            ptr1 = ptr1.next
        ptr2.next = ptr2.next.next
        return head'''