# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:36:27 2020
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
@author: lenovo

    '''
    def reverse(self, head):
        prev = None
        curr = head
        if curr == None or curr.next == None:
            return head
        following = curr.next
        
        while curr:
            curr.next = prev
            prev=curr
            curr=following
            if following:
                following=following.next
                
        head = prev
        return head
    
    def isPalindrome(self, head: ListNode) -> bool:
        #intuition :- that traverse till mid and then pop after if the elements are same. basically the stack should be empty if the list ends.
        curr=head
        result = self.reverse(curr)
        while curr:
                if curr.val == result.val:
                    curr = curr.next
                    result = result.next
                else:
                    return False
        return True
            '''
            
        
    
   
            
        
'''
        time  and space = O(n)
        res = []
        pointer = head
        while pointer:
            res.append(pointer.val)
            pointer=pointer.next
        for i in range(len(res)//2):
            if res[i]!=res[len(res)-i-1]:
                return False
        return True '''
                
        '''s = stack()
        ptr1 = head
        ptr2 = head
        while ptr2:
            ptr1=ptr1.next
            ptr2=ptr2.next.next
            s.push(ptr1)
        while(ptr1):
            if ptr1.val==s.top():
                s.pop()
            ptr1=ptr1.next
        if s.isempty():
            return True
        return False'''
       
"""

#10.18 Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        fast = head
        slow = reverse(slow)
        
        while slow:
            if fast.val != slow.val:
                return False
            
            fast = fast.next
            slow = slow.next
            
        return True
    
def reverse(head):
    current = head
    prev, next = None, None
    
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
        
    return prev



"""
lightweight solution interviewbit

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        count = 0
        node = A
        while node:
            count += 1
            node = node.next
        prev = None
        curr = A
        for i in range(count // 2):
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        if count % 2 == 1:
            curr = curr.next
        while curr:
            if curr.val != prev.val:
                return 0
            curr = curr.next
            prev = prev.next
        return 1
"""
