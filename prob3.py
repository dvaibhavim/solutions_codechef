# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:06:34 2020

@author: lenovo
"""

'''Write a program, which takes an integer N and if the number is less than 10 then display "What an obedient servant you are!" otherwise print "-1".

Input
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

Output
Output the given string or -1 depending on conditions.

Constraints
1 ≤ T ≤ 1000
-20 ≤ N ≤ 20
Example
Input
3 
1
12
-5
Output
What an obedient servant you are!
-1
What an obedient servant you are!
'''

T = int(input())
for tc in range(T):
    n = int(input())
    print("What an obedient servant you are!") if n<10 else print(-1)