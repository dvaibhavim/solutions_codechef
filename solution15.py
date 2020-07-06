# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:32:26 2020

@author: lenovo

Question 3: Given an array l and a query q, find a pair in the array which have a sum equals to q.

for e.g. l = [16, 17, 4, 3, 5, 2] and q = 7

answer: (4,3)

Question 4: Print the nodes in a binary tree level-wise. For example, the following 

  1
 / \
2   3
   / \
  4   5

should print 1, 2, 3, 4, 5.
"""

l = [1, 2, 3, 4, 5]
q=7
sum_q = 0
for i in l:
    for j in range(i+1,len(l)-1):
                if l[i]+l[j]==q:
                    print(l[i],l[j])   
#    if i<q and  i+(i+1)==q :
#        print(i,i+1)
#        flag = 1
#    else:
#        sum_q = i

#if flag==0:
         