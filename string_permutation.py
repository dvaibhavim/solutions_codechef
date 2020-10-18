# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:40:18 2020
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

@author: lenovo
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        s1_word_counter = Counter(s1)
        window = Counter(s2[:window_size])
        if window == s1_word_counter:
            return True
            
        for idx in range(1,len(s2)-window_size + 1):
            minus = {s2[idx-1]:1}
            plus = {s2[idx+window_size-1]:1}
            print(minus,plus)
            window -= minus
            window += plus
            print(window,s1_word_counter)
            if window == s1_word_counter:
                return True
        return False
