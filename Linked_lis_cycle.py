# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 18:17:35 2020

@author: lenovo
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.

Example :

Input : 

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3. 

my output

Time Limit Exceeded. Your submission didn't complete in the allocated time limit.

IN AN ACTUAL INTERVIEW, THE SOONER YOU ARRIVE AT THE MOST OPTIMAL SOLUTION, THE BETTER. IN GENERAL, TRY TO CORRECTLY ESTIMATE THE TIME COMPLEXITY OF YOUR SOLUTION.

Your submission timed out for the following input:
11 87797 23219 41441 58396 48953 94603 2721 95832 49029 98448 65450
-1
There are 2 lines in the input

Line 1 ( Corresponds to arg 1 ) : Elements in the linked list. First number S is the number of nodes. Then S numbers follow indicating the val in each of the nodes in sequence
	For example, LinkedList: "5 --> 9 --> 7" will be written as "3 5 9 7"(without quotes).

Line 2 : Integer X corresponding to a node position. If the integer is -1, then there is no loop. Otherwise, the end node has a next edge to node number X.
	For example, Integer: "-1" will be written as "-1"(without quotes).
The expected output for this testcase is:
NULL
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        curr = A
        #check if there's one 1 element, then return head else point node to next element else both curr and node will be head and it will always return true.
        if A.next:
            node = A.next
        else:
            return A
        
        #using set since it is given Try solving it using constant additional space.
        s = set()
        while curr:
            if curr not in s:
                s.add(curr)
                curr = curr.next
            else:
                return curr
        return None
