''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT


''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def isSafe(M, row, col, visited): 
    global ROW, COL 
      
    # row number is in range, column number is in  
    # range and value is 1 and not yet visited  
    return ((row >= 0) and (row < ROW) and
            (col >= 0) and (col < COL) and 
            (M[row][col] and not visited[row][col])) 
  
# A utility function to do DFS for a 2D  
# boolean matrix. It only considers  
# the 8 neighbours as adjacent vertices  
def DFS(M, row, col, visited, count): 
      
    # These arrays are used to get row and column  
    # numbers of 8 neighbours of a given cell  
    rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]  
    colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]  
  
    # Mark this cell as visited  
    visited[row][col] = True
  
    # Recur for all connected neighbours  
    for k in range(8): 
        if (isSafe(M, row + rowNbr[k],  
                   col + colNbr[k], visited)): 
                         
            # increment region length by one  
            count[0] += 1
            DFS(M, row + rowNbr[k],  
                col + colNbr[k], visited, count) 
  
# The main function that returns largest 
# length region of a given boolean 2D matrix  
def largestRegion(M): 
    global ROW, COL 
      
    # Make a bool array to mark visited cells.  
    # Initially all cells are unvisited  
    visited = [[0] * COL]*ROW
  
    # Initialize result as 0 and travesle  
    # through the all cells of given matrix  
    result = -999999999999
    for i in range(ROW): 
        for j in range(COL): 
              
            # If a cell with value 1 is not  
            if (M[i][j] and not visited[i][j]): 
                  
                # visited yet, then new region found  
                count = [1]  
                DFS(M, i, j, visited, count)  
  
                # maximum region  
                result = max(result, count[0]) 
    return result 
ROW,COL = map(int,input().split(' '))
arr=[]
for _ in range(ROW):
    arr.append(input().split(' '))
arr = [list(map(int,i)) for i in arr]
print(largestRegion(arr))
#def main():

 # Write code here 

#main()

