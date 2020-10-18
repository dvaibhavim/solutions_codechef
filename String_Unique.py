# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:49:34 2020

check whether the string has all unique characters.
@author: lenovo
"""
s = input()
result = sorted(s)
print(result)
def IsUnique(s):
    if s == None:
        return False
    for i in range(len(s)-1):
       if s[i]==s[i+1]:
           return False
           break
    return True
print(IsUnique(result))
        

