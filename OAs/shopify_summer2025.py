

array1 = [
    ["A", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["B", "B", "B", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "C", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "C", "D", "D", "D", "D", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", "E", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", "E", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", "F", "F", "F", "F", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", "G", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", "K", "G", "G", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
]


def move_up(cur):
    return [cur[0]-1, cur[1]]
def move_down(cur):
    return [cur[0]+1, cur[1]]
def move_left(cur):
    return [cur[0], cur[1]-1]
def move_right(cur):
    return [cur[0], cur[1]+1]
sol=[]
visited=[[False for i in range(15)] for j in range(10)]
def dfs(cur, grid):
    print(cur, 'cur', visited[cur[0]][cur[1]])
    if cur[0]<0 or cur[1]<0 or cur[0]>9 or cur[1]>14:
        print('not in')
        return
    if visited[cur[0]][cur[1]]:
        print('visited')
        return
    if grid[cur[0]][cur[1]] == " ":
        print('blank')
        return
    
    if grid[cur[0]][cur[1]] != "*":
        sol.append(grid[cur[0]][cur[1]])
    visited[cur[0]][cur[1]] = True
    
    dfs(move_up(cur), grid)
    dfs(move_down(cur), grid)
    dfs(move_left(cur), grid)
    dfs(move_right(cur), grid)


dfs([0, 0], array1)
print(sol)
