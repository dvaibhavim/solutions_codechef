"""
Chef likes all arrays equally. But he likes some arrays more equally than others. In particular, he loves Rainbow Arrays.

An array is Rainbow if it has the following structure:

First a1 elements equal 1.
Next a2 elements equal 2.
Next a3 elements equal 3.
Next a4 elements equal 4.
Next a5 elements equal 5.
Next a6 elements equal 6.
Next a7 elements equal 7.
Next a6 elements equal 6.
Next a5 elements equal 5.
Next a4 elements equal 4.
Next a3 elements equal 3.
Next a2 elements equal 2.
Next a1 elements equal 1.
ai can be any non-zero positive integer.
There are no other elements in array.

Help Chef in finding out if the given array is a Rainbow Array or not.

t= int(input())
for j in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    cnt=0
    for i in range(n):
        if arr[i]==arr[n-i-1]:
            cnt+=1 
    print(cnt,max(arr))
    if cnt == n:
        print("yes")
    else:
        print("no")
  """      
        
# cook your dish here
T=int(input())
ind=[1,2,3,4,5,6,7]
for i in range(T):
    N=int(input())
    lis=list(map(int,input().split()))
    lis1=list(set(lis))
    ans='yes'
    if lis1!=ind:
        ans='no'
    else:
        for j in range(N//2):
            if (lis[j]>7 or (lis[j+1]-lis[j])<0 or (lis[j+1]-lis[j])>1 or lis[j]!=lis[N-j-1]):
                ans='no'

    print(ans)
               
      
            
        
    
    
  
        
            



        

        