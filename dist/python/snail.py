# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
# --------------------------------- SOLUTION --------------------------------- #
def snail(snail_map):
    res = []
    if not snail_map or not snail_map[0]:
        return res
    
    top, bottom = 0, len(snail_map) - 1
    left, right = 0 , len(snail_map) - 1

    while top<=bottom and left <= right:

        #move right
        for i in range(left, right + 1):
            res.append(snail_map[top][i])
        top += 1

        #move down
        for i in range(top, bottom + 1):
            res.append(snail_map[i][right])
        right -= 1

        #move left
        if top<= bottom:
            for i in range(right, left - 1, -1):
                res.append(snail_map[bottom][i])
            bottom -= 1

        #move up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(snail_map[i][left])
            left += 1
    return res

# 2nd way
def snail(matrix):
    if not matrix or not matrix[0]: return []
    
    n = len(matrix)
    # Directions: Right, Down, Left, Up
    # These are your "switchers" for i and j
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    r, c = 0, 0 # Current position
    di = 0      # Current direction index (starts at Right)
    res = []
    
    # Track visited cells to know when to "switch"
    visited = [[False] * n for _ in range(n)]
    
    for _ in range(n * n):
        res.append(matrix[r][c])
        visited[r][c] = True
        
        # Predict next position
        next_r = r + dr[di]
        next_c = c + dc[di]
        
        # Check boundary or if already visited
        if 0 <= next_r < n and 0 <= next_c < n and not visited[next_r][next_c]:
            r, c = next_r, next_c
        else:
            # Hit a wall! Change direction (The Switcher)
            di = (di + 1) % 4
            r += dr[di]
            c += dc[di]
            
    return res

# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
if expected == snail(array) :
    print('Correct', snail(array))
else:
    print ('ERROR' , snail(array))