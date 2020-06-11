# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:31:27 2020

Three numbers A, B and C are the inputs. Write a program to find second largest among three numbers.
Input
The first line contains an integer T, total number of testcases. 
Then follow T lines, each line contains three integers A, B and C.
"""
#T=int(input())
#for tc in range(T):
#    a=(input().split(' '))
#    a = sorted(a)[-2]
#    print(a)


T=int(input())
for tc in range(T):
    a,b,c=map(int, input().split(' '))
    a = (a,b,c)

    print(sorted(a)[-2])

