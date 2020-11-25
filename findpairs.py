"""
Pairs with Specific Difference
Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

Examples:

input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []
Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 100
[input]integer k

k ≥ 0
[output] array.array.integer


[0, -1, -2, 2, 1]

x - y = k
[0, -1, -2, 2, 1]


x = 1

-y  = k - x
0: 0, -1: 1, -2: 2, 2:3 , 1: 4

1 , -1 -> -1 - y = k - x
curr = 0 -> 1 - 0
1 - x = 

- 1 -> 1 + ()
iTH = k + ith

{0: T, -1: T, -2: T, 1: T}

0 > 0 - 1
-1 > -1 -1 -> -2
-2 -> -2 -1 -> -3 
2 : -> 2 - 1 -> 1
1: 1-1 -> 0


0 -> 1
-1 -> 0

"""
from collections import defaultdict
def find_pairs_with_given_difference(arr, k):
  element_map = {val: index for index,val in enumerate(arr) }
  res = []
  
  
  for y in arr: 
    x = k + y
    if x in element_map:
      res.append([x, y])
    else:
      element_map[y] = True
      
  return res
      