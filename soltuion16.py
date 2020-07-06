# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:22:53 2020

@author: lenovo
"""

def generalizedGCD(x, y):
    # WRITE YOUR CODE HERE
    while(y):
        x,y = y, x%y 
        return x 
        
num = int(input())
arr = input()
arr = arr.strip("[]")
arr = list(arr.split(','))

arr = [int(arr[i]) for i in range(num)]
print(arr)
num1 = arr[0]
num2 = arr[1]
gcd = generalizedGCD(num1,num2)

for i in range(2,num):
    gcd = generalizedGCD(gcd,arr[i])


print(gcd)