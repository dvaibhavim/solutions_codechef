def index_equals_value_search(arr):
  #[0,1]
  left = 0
  #if len(arr)==1:
  #  return arr[0]
  right = len(arr)-1
  index = 0
  last = -1
  while left<=right:
    index = (left+right)//2
    if arr[index]-index<0:
      left = index +1
    elif arr[index]==index:
      last = index
      right = index-1
    else:
      right = index-1
    #if arr[left]==left:
    #  return left
  return last
      
  
  
  
  """
  for i in range(len(arr)): 
    if arr[i]==i:
      return i
    
  return -1
  """
  
  
  





"""
 0 1 2 3 4 5 
[1,2,3,4,5,6]

mid = len(arr)/2
left = arr,mid,index
right = arr,min, end, index

ex=[-8,0,2,5]

"""