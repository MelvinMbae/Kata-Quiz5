def solution (blocks):
    n = len(blocks)
    
    # Positional variables
    
    # Start
    left = 0
    
    # End
    right = n-1
    
    maximum_distance = 0
    
    while left <= right:
        # minimum_height = min(blocks[right])
        maximum_distance = max(maximum_distance,(right - left ))
        if blocks[left] < blocks[right]:
            left +=1
        else: right -=1
        
    return maximum_distance

blocks = [1,1]
print(solution(blocks))