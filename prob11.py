# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:21:00 2020

https://www.codechef.com/problems/AMR15A

Mahasena 

Input
The first line of input consists of a single integer N denoting the number of soldiers. 
The second line of input consists of N space separated integers A1, A2, ..., AN, where Ai denotes the number of weapons that the ith soldier is holding.

Output
Generate one line output saying "READY FOR BATTLE", if the army satisfies the conditions that Kattapa requires 
or "NOT READY" otherwise (quotes for clarity).
"""

def even_soldier(n):
    even = [i for i in n if i%2==0]
    odd = [i for i in n if i%2!=0]
    if len(even)>len(odd):
        return "READY FOR BATTLE"
    else:
        return "NOT READY"
    
n = int(input())
weapons =input().split(' ')
weapons = list(map(int,weapons))
result = even_soldier(weapons)
print(result)
    