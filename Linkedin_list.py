# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:17:19 2020
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
@author: lenovo
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) :
        us = set()
        current = head
        prev = head
        while(current!=None):
            if current.val in us:
                prev.next=current.next
                del(current)
            else:
                us.add(current.val)
                prev=current
            current=prev.next
        return head
        