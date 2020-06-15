# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:14:02 2020
COVID Pandemic and Long Queue 


Input
The first line of the input contains a single integer T denoting the number of test cases. 
The description of T test cases follows.
The first line of each test case contains a single integer N.
The next line contains N space-separated integers A1,A2,…,AN.
Output
For each test case, print a single line containing the string "YES" if 
social distancing is being followed or "NO" otherwise (without quotes).
"""

# =============================================================================
# t = int(input())
# result = []
# for tc in range(t):
#     n = input()
#     distance = input().split(' ')
#     index_1 = [i for i in range(len(distance)) if int(distance[i])==1]
#     result.append(check_distance(index_1))
# 
# for i in result:
#     print(i)
# 
# 
# def check_distance(index_1):
#     for i in range(len(index_1)-1):
#         if index_1[i+1]-index_1[i]==6:
#             continue
#         else:
#             print("NO")
#             break
#         if i+1 == len(index_1):
#             print("YES")
# =============================================================================


try:
 n=int(input())
 for i in range(n):
    t=int(input())
    s=list(map(int,input().split()))
    c=[]
    flag=0
    for j in range(len(s)):
         if(s[j]==1):
            c.append(j+1)
    for j in range(len(c)-1):
        if(c[j+1]-c[j]<6):
            flag=1
            break
    if(flag==1):
        print("NO")
    else:
        print("YES")
except EOFError:
    pass