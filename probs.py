# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:28:59 2020

@author: lenovo
"""

#t = int(input())
#for tc in range(t):
#    digit = input()
#    sum_digit = (int(i) for i in digit )
#    print(sum(sum_digit))
    
    
import math as m
T = int(input())
for tc in range(T):
    (a,b) = map(int,input().split(' '))
    print(m.remainder(a,b))    