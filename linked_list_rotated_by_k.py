
'''
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

Runtime: 36 ms, faster than 68.14% of Python3 online submissions for Rotate List.
Memory Usage: 14.1 MB, less than 72.54% of Python3 online submissions for Rotate List.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        node = head
        last = None
        length = 0
        if head is None or head.next is None:
            return head
        while node:
            last = node
            length+=1
            node=node.next
            
        k%= length
        if k==0:
            return head
        curr = head
        for i in range(length-k-1):
            curr = curr.next
        rotated_head = curr.next    
        curr.next=None
        last.next = head        
        return rotated_head
        
            
        