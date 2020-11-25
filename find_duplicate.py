'''
Find The Duplicates
Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.

Example:

input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

output: [3, 6, 7] # since only these three values are both in arr1 and arr2
Constraints:

[time limit] 5000ms

[input] array.integer arr1

1 ≤ arr1.length ≤ 100
[input] array.integer arr2

1 ≤ arr2.length ≤ 100
[output] array.integer

'''
  
  input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

arr1 = set([3,3,4])
arr2 set([ 4,4,2])

arr1 = []
arr2=[3,4,5]
arr1 = [1,2,3]
arr2 = []
output: [3, 6, 7] #
for i in arr1
set[i] +=1

time = o(nlogn)
space = k number of intersection
  '''

def find_duplicates(arr1, arr2):
  result =sorted(list(set(arr1) & set(arr2)) )#&
  return result

def find_duplicates(arr1, arr2):
  pointer1 = 0
  pointer2 = 0
  result = []
  while pointer1 < len(arr1) and pointer2 < len(arr2):
    if arr1[pointer1] < arr2[pointer2]:
      pointer1 +=1
      
    elif arr1[pointer1] > arr2[pointer2]:
      pointer2 += 1
      
    else:
      result.append(arr1[pointer1])
      pointer1 += 1
      pointer2 += 1
  return(result)