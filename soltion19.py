# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:13:51 2020

https://www.codechef.com/problems/CHN15A

Mutated Minions 
Gru has not been in the limelight for a long time and is, therefore, planning something particularly nefarious. Frustrated by his minions' incapability which has kept him away from the limelight, he has built a transmogrifier — a machine which mutates minions.

Each minion has an intrinsic characteristic value (similar to our DNA), which is an integer. The transmogrifier adds an integer K to each of the minions' characteristic value.

Gru knows that if the new characteristic value of a minion is divisible by 7, then it will have Wolverine-like mutations.

Given the initial characteristic integers of N minions, all of which are then transmogrified, find out how many of them become Wolverine-like.

Input Format:
The first line contains one integer, T, which is the number of test cases. Each test case is then described in two lines.

The first line contains two integers N and K, as described in the statement.

The next line contains N integers, which denote the initial characteristic values for the minions.

Output Format:
For each testcase, output one integer in a new line, which is the number of Wolverine-like minions after the transmogrification.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100
1 ≤ K ≤ 100
All initial characteristic values lie between 1 and 105, both inclusive.
Example
Input:
1
5 10
2 4 1 35 1

Output:
1
@author: lenovo
"""
# cook your dish here
#cnt = []
t = int(input())
while(t):
    n,k = tuple(map(int,input().split()))
    minion = tuple(map(int,input().split()))
    if n == len(minion):
        pass
    else:
        print("len of n not matching with minions")
    new_minion = (i+k for i in minion)
    cnt = 0
    for j in new_minion:
        if j%7==0:
            cnt+= 1 
    print(cnt)       
    t-=1 
