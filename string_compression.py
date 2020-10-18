# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:27:59 2020

@author: lenovo
"""

# =============================================================================
# def stringCompress(message):
#     i = 0
#     encoded_message=""
#     while (i <= len(message)-1): 
#         count = 1
#         ch = message[i] 
#         j = i 
#         while (j < len(message)-1): 
#             if (message[j] == message[j+1]): 
#                 count = count+1
#                 j = j+1
#             else: 
#                 break
#         encoded_message=encoded_message+ch+str(count) 
#         i = j+1
#     return encoded_message
# =============================================================================


def stringCompress(str1):
  str_count = {}
  x = []
  if str1==None:
      return False
  for i in str1:
      cnt=0
      if i not in str_count.keys():
          str_count[i] =  cnt + 1
      else:
          str_count[i] = str_count[i]+1
  for key,val in str_count.items():
      x.append(key)
      x.append(val)
  for i in x[1::2]:
        x[i] = str(x[i])
  return(''.join(map(str, x)))
str1 = "happy"
print(stringCompress(str1))
        