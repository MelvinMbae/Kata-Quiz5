def solution (blocks):
    n = len(blocks)
    
    left = 0
    right = n-1
    
    maximum_distance = 0
    
    while left <= right: