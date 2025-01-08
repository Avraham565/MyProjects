
"""
Assignment Title: Counting the Number of Islands

Background:
In computer science, the "Number of Islands" problem is a classic graph traversal problem 
that involves identifying distinct clusters in a grid. The task simulates real-world applications 
like image processing, social network analysis, and geographic mapping.

Problem Statement:
You are given a 2D grid of '1's (land) and '0's (water). An island is surrounded by water and is formed 
by connecting adjacent lands horizontally or vertically. You need to determine the number of islands 
in the given grid.

Task:
Write a Python function `count_islands(grid: List[List[str]]) -> int` that takes a 2D grid as input 
and returns the total number of distinct islands.

Input:
- A 2D grid represented as a list of lists of strings, where:
  - '1' represents land.
  - '0' represents water.
- The grid dimensions are at most 300 x 300.

Output:
- An integer representing the number of islands.

Example:

Input:
grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
]

Output:
3

Explanation:
- Island 1: Formed by the top-left cluster of '1's.
- Island 2: Formed by the middle '1'.
- Island 3: Formed by the bottom-right cluster of '1's.

Constraints:
1. The grid can contain only the characters '1' and '0'.
2. You may assume all four edges of the grid are surrounded by water.
3. The grid may contain no land ('1'), in which case the output should be 0.

Guidelines:
1. Implement the solution using either Depth-First Search (DFS).
2. Avoid visiting the same cell more than once. Use a mechanism (e.g., marking visited cells) 
   to keep track of visited land cells.
3. Test your solution with edge cases, such as an empty grid, a grid with no islands, or a grid with a single island.

Bonus Challenges:
1. Optimize the solution for memory usage in large grids.
2. Modify the function to allow diagonal connections (i.e., islands connected diagonally are considered part of the same island).
3. Visualize the grid and the islands using a plotting library like Matplotlib.

Submission:
- Save your solution in a Python file named `number_of_islands.py`.
- Include comments explaining your approach and any assumptions.
- Test your code with at least five unique test cases and include them in a separate file named `test_number_of_islands.py`.
"""

from typing import List

grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
]

def dfs_without(grid,row,col,visited):
    if row<0 or col< 0 or row >= len(grid) or col >= len(grid[0]):
        return
    if visited[row][col] or grid[row][col] == "0":
        return
    visited[row][col] = True
    dfs_without(grid,row-1,col,visited)
    dfs_without(grid,row+1,col,visited)
    dfs_without(grid,row,col-1,visited)
    dfs_without(grid,row,col+1,visited)

def count_islands_without(grid: List[List[str]]) -> int:
    counter = 0
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if not visited[row][col] and grid[row][col] == "1":
              counter+=1
              dfs_without(grid,row,col,visited)       
    return counter

print(count_islands_without(grid))

def dfs(grid,row,col,visited):
    if row<0 or col< 0 or row >= len(grid) or col >= len(grid[0]):
        return
    if visited[row][col] or grid[row][col] == "0":
        return
    visited[row][col] = True
    dfs(grid,row-1,col,visited)
    dfs(grid,row+1,col,visited)
    dfs(grid,row,col-1,visited)
    dfs(grid,row,col+1,visited)
    dfs(grid,row-1,col-1,visited)
    dfs(grid,row+1,col+1,visited)
    dfs(grid,row+1,col-1,visited)
    dfs(grid,row-1,col+1,visited)

def count_islands(grid: List[List[str]]) -> int:
    counter = 0
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if not visited[row][col] and grid[row][col] == "1":
              counter+=1
              dfs(grid,row,col,visited)       
    return counter

print(count_islands(grid))