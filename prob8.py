# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:06:18 2020

Consider a currency system in which there are notes of six denominations, namely, Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100.
If the sum of Rs. N is input, write a program to computer smallest number of notes that will combine to give Rs. N.
Input
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

Output
Display the smallest number of notes that will combine to give N.

Constraints
1 ≤ T ≤ 1000
1 ≤ N ≤ 1000000
Example
Input
3 
1200
500
242

Output
12
5
7
"""

try:
    t=int(input(''))
    list=[100,50,10,5,2,1]
    while t>0:
        count=0
        n=int(input(''))
        for i in list:
            if n/i!=0:
             count=count+int(n/i)
             n=int(n%i)
        print(count)
        t=t-1

except Exception as e:
    pass