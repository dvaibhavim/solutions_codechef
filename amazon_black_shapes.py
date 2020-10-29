'''
Given N x M character matrix A of O's and X's, where O = white, X = black.

Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)



Input Format:

    The First and only argument is a N x M character matrix.
Output Format:

    Return a single integer denoting number of black shapes.
Constraints:

    1 <= N,M <= 1000
    A[i][j] = 'X' or 'O'
Example:

Input 1:
    A = [ OOOXOOO
          OOXXOXO
          OXOOOXO  ]
Output 1:
    3
Explanation:
    3 shapes are  :
    (i)    X
         X X
    (ii)
          X
    (iii)
          X
          X
Note: we are looking for connected shapes here.

XXX
XXX
XXX
is just one single connected black shape.

'''

class Solution:
class Solution:
	# @param A : list of strings
	# @return an integer
	def black(self, A):
	   def dfs(arr,i, j ,visit,r,c):
	       if i>=0 and j>=0 and i<r and j<c and arr[i][j] == 'X' and not visit[i][j]:
	           visit[i][j]=True
    	       dfs(arr,i+1,j,visit,r,c)
    	       dfs(arr,i-1,j,visit,r,c)
    	       dfs(arr,i,j+1,visit,r,c)
    	       dfs(arr,i,j-1,visit,r,c)
	       
	       
	    
	   row = len(A)
	   column = len(A[0])
	   count = 0
	   visit = [ [False for j in range(column)] for i in range(row)]
	   for i in range(row):
	       for j in range(column):
	           if A[i][j]=='X' and not visit[i][j]:
	               dfs(A,i,j,visit,row,column)
	               count +=1
	               
	   return count