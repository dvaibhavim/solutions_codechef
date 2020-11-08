'''
Pairs with Specific Difference
'''



def find_pairs_with_given_difference(arr, k):
    if k == 0:
        return []
        
    map = {}
    answer = []
    
    for x in arr:
        map[x - k] = x
    
    for y in arr:
        if y in map:
            answer.append([map[y], y]) 

    return answer
        
