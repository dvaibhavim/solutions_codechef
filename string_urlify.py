# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:42:10 2020
URLify a given string (replace spaces with %20)

Questions:

How is Hashmap implemented, time complexities, details about how hash function works.
What is a BST, what is the time complexities
What algorithm you use to convert a BST that has only right children (sorted array)
Challenging work you have done in past.
Merge sort vs Quick sort, about their time complexities, which is preferable when sorting a large data set.
Write a method to replace all the spaces in a string with ‘%20’. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the “true” length of the string.

@author: lenovo
"""

def ReplaceSpaces(str1: [str], length: int) -> str:
    spacecount = 0
    #print(type(str1))
    for i in range(length):
        if str1[i]==' ':
            spacecount +=1
    newLength = length +spacecount*2
    print(newLength,spacecount)
    #start replacing the space from backwards
    for j in range(length-1,0,-1):
        #j = length-i
        print(str1[j])
        if str1[j]==' ':
            str1[newLength-1]='0'
            str1[newLength-2]='2'
            str1[newLength-3]='%'
            newLength = newLength-3
            print(str1)
        else:
            str1[newLength-1]=str1[j]
            newLength -=1
    return "".join(str1)
        
#print(ReplaceSpaces("Mr John Smith       ", 13))

str1 = list(input())
length = int(input())       
print(ReplaceSpaces(str1,length))     