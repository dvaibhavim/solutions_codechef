# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:38:49 2020

What is the maximum number of squares of size 2x2 that can be fit in a right angled isosceles triangle of base B.
One side of the square must be parallel to the base of the isosceles triangle.
Base is the shortest side of the triangle
"""

t=int(input())
for i in range (t):
     ele=int(input())
     n=ele//2
     print(n*(n-1)//2)
     
     
 '''
t = int(input())
for _ in range(t):
    b = int(input())
    b = (b - 2) 
      
    # Since each square has base of 
    # length of 2 
    b = b // 2
      
    print(int(b * (b + 1) / 2))
    
    
    T = int(input())
for _ in range(T):
    n = int(input())
    print((n // 2) * ((n // 2) - 1) // 2)
    
    
    for T in range(int(input())):
    B= int(input())
    N= (B//2)-1
    res= (N*(N+1))//2
    print(res)
'''    