# Apply Graph traversal to solve a problem (Portfolio Project Problem): 

You are given a 2-D puzzle of size MxN, that has N rows and M column (N >= 3 ; M >= 3; M and N can be different).
Each cell in the puzzle is either empty or has a barrier. An empty cell 
is marked by ‘-’ (hyphen) and the one with a barrier is marked by ‘#’. You are given two 
coordinates from the puzzle (a,b) and (x,y). You are currently located at (a,b) and want to 
reach (x,y).
You can move only in the following directions:
* L: move to left cell from the current cell 
* R: move to right cell from the current cell 
* U: move to upper cell from the current cell 
* D: move to the lower cell from the current cell 
 
You can move to only an empty cell and cannot move to a cell with a barrier in it. Your goal 
is to find the minimum number of cells that you have to cover to reach the destination cell 
(do not count the starting cell and the destination cell). The coordinates (1,1) represent the 
first cell; (1,2) represents the second cell in the first row. If there is not possible path from 
source to destination return None. 

Sample Input Puzzle Board: `[[-,-,-,-,-],[-,-,#,-,-],[-,-,-,-,-],[#,-,#,#,-],[-#,-,-,-]]`
 
* Example 1: (a,b) : (1,3) → (x,y): (3,3)
  - Output: 3 
  - On possible direction to travel: LDDR, (1,3) → (1,2) → (2,2) → (3,2) → (3,3) 
 
* Example 2: (a,b): (1,1) → (x,y): (5,5)
  - Output: 7
  - One possible direction to travel: DDRRRRDD, (1,1) → (2,1) → (3,1) → (3,2) → (3,3) → (3,4) → (3,5) → (4,5) → (5,5) 
 
* Example 3: (a,b): (1,1) → (x,y) : (5,1)
  - Output: None 
 
a. Describe an algorithm to solve the above problem.

  1. Get the row and col count for the Board.
  2. Using another function, perform a BFS by:
     - keeping track of the source and then the neighboring nodes in a deque
     - keeping track of whether the location has been visited
     - keeping track of the previous location prior to coming to the neighbor
  3. While we still have neighbors and have not reached the destination square:
     - pop the the first square in the queue
     - for each of the the directions: left, up, down, right
     - calculate the neighbor and check whether it is valid and not visited and
  not blocked
     - If the previous is valid, mark the neighbor as visited, update its previous
  direction as the current node, and add it to the queue
     - if the neighbor is the destination, then we can break early and begin
  reporting the path
     - else continue and repeat
  4. Finally, take the previous data structure built and reconstruct the path by taking
  the previous steps/direction taken and return the result.

b. Implement your solution in a function solve_puzzle(Board, Source, Destination).
Name your file Puzzle.py

c. What is the time complexity of your solution?

 In worst case, the time taken to traverse the matrix is by visiting each cell is mn.
 This implementation uses a regular deque that has queue and dequeue operations
 of O(1) as there is no priority given for cells, they just need to be empty to visit. We
 also only visit each cell once, as it is marked as visited and thus, the time
 complexity is: O(m ⋅ n)
 
d. (Extra Credit): For the above puzzle in addition to the output return a set of possible 
directions as well in the form of a string. 
For above example 1 Output: 7, LDDR 
