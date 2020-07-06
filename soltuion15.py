# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:15:22 2020

@author: lenovo


Question 1. Write a program to print all the LEADERS in the array. An element is leader if it is greater than all the elements to its right side. And 
the rightmost element is always a leader. For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.

Let the input array be arr[] and size of the array be size.
"""

arr = [16, 17, 4, 3, 5, 2]

max_arr = []
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<=arr[j]:
            break            
    if j == len(arr)-1:
        max_arr.append(arr[i])
    
print(max_arr)
