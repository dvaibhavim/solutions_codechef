# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:03:00 2020

@author: lenovo
"""

arr =  ["red","red","yellow","green","red","yellow","green","green","yellow","purple"]
val = {}

for i in arr:
    val[str(i)] = arr.count(i)


print(sorted(list(val.keys()))[:-1][0])
#print(val)
    
# =============================================================================
# print(sorted(val.values()))
# =============================================================================
