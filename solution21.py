# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:37:22 2020
There are 100 houses located on a straight line. The first house is numbered 1 and the last one is numbered 100. Some M houses out of these 100 are occupied by cops.

Thief Devu has just stolen PeePee's bag and is looking for a house to hide in.

PeePee uses fast 4G Internet and sends the message to all the cops that a thief named Devu has just stolen her bag and ran into some house.

Devu knows that the cops run at a maximum speed of x houses per minute in a straight line and they will search for a maximum of y minutes. Devu wants to know how many houses are safe for him to escape from the cops. Help him in getting this information.

Input
First line contains T, the number of test cases to follow.

First line of each test case contains 3 space separated integers: M, x and y.

For each test case, the second line contains M space separated integers which represent the house numbers where the cops are residing.

Output
For each test case, output a single line containing the number of houses which are safe to hide from cops.

Constraints
1 ≤ T ≤ 104
1 ≤ x, y, M ≤ 10
Example
Input:
3
4 7 8
12 52 56 8
2 10 2
21 75
2 5 8
10 51

Output:
0
18
9
@author: lenovo
"""

for _ in range(int(input())):
    s = set(range(1,101))
    m,x,y = map(int,input().split())
    d = x*y
    for i in map(int,input().split()):
        lower_limit = [1,i-d][i-d>1]
        upper_limit = [100,i+d][i+d<100]
        s -= set(range(lower_limit,upper_limit+1))
    print(len(s))
