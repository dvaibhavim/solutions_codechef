# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:05:30 2020

palindrome problem
minimum number of steps to make the word palindrome
"""





def checkpalindrome(string):
    return string==string[::-1]
    
flag = 0
cnt = 0
string = input()
for i in range(len(set(string))):
    print(string[i],string.count(string[i]))
    
while(len(string)>0):
    if(checkpalindrome(string)):
        flag=1
        break
    else:
        cnt +=1
        string=string[:-1]
if flag:
    print(cnt)    
    

