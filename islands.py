n = int(input())
islands = []
visited = []
for i in range(n):
    islands += [input().split(" ")]
    visited += [[0] * n]

island_and_coast = {}
number_of_coast = 1

def dfs(index_row, index_column, number_of_water):
    if index_row != 0:
        if islands[index_row-1][index_column] == '-' and visited[index_row-1][index_column] == 0:
                number_of_water += 1
                visited[index_row - 1][index_column] = 1
        elif islands[index_row-1][index_column] == '#' and visited[index_row-1][index_column] == 0:
            visited[index_row-1][index_column] = 1
            dfs(index_row-1, index_column, number_of_water)
        
    if index_row != n-1:
        if islands[index_row+1][index_column] == '-' and visited[index_row+1][index_column] == 0:
            number_of_water += 1
            visited[index_row + 1][index_column] = 1
        elif islands[index_row+1][index_column] == '#' and visited[index_row+1][index_column] == 0:
            visited[index_row+1][index_column] = 1 
            dfs(index_row+1, index_column, number_of_water)

    if index_column != 0:
        if islands[index_row][index_column-1] == '-' and visited[index_row][index_column-1] == 0:
            number_of_water += 1
            visited[index_row][index_column - 1] = 1
        elif islands[index_row][index_column-1] == '#' and visited[index_row][index_column-1] == 0:
            visited[index_row][index_column-1] = 1
            dfs(index_row, index_column-1, number_of_water)
        
    if index_column != n-1:
        if islands[index_row][index_column+1] == '-' and visited[index_row][index_column+1] == 0:
            number_of_water += 1
            visited[index_row][index_column + 1] = 1
        elif islands[index_row][index_column+1] == '#' and visited[index_row][index_column+1] == 0:
            visited[index_row][index_column+1] = 1
            dfs(index_row, index_column+1, number_of_water)
    
    return number_of_water

for index_row in range(n):
    for index_column in range(n):
        if islands[index_row][index_column] == '#' and visited[index_row][index_column] == 0:
            number_of_water = 0
            visited[index_row][index_column] = 1
            water_surround = dfs(index_row, index_column, number_of_water)
            island_and_coast[number_of_coast] = water_surround
            number_of_coast += 1 

print(island_and_coast)
