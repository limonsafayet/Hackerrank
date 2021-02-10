# Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along
# with an integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i + j + k is not equal
# to n. Here, 0 <= i <= x; 0<= j <= y; 0<= k <= z. Please use list comprehensions rather than multiple loops, as a learning exercise.
# Example
# x = 1
# y = 1
# z = 2
# n = 3 

# All permutations of [i,j,k] are:
# [[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[0,1,2],[1,0,0],[1,0,1],[1,0,2],[1,1,0],[1,1,1],[1,1,2]]
# Print an array of the elements that do not sum to n = 3.
# [[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,2]]

# Input Format

# Four integers x,y,z and n, each on a separate line.

# Constraints

# Print the list in lexicographic increasing order.

# Sample Input 0

# 1
# 1
# 1
# 2
# Sample Output 0

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Explanation 0

# Each variable x,y and z will have values of 0 or 1. All permutations of lists in the form 
# [i,j,k] = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]].
# Remove all arrays that sum to n = 2 to leave only the valid permutations.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    ListOf_x = [ a for a in range(x+1) ] 
    ListOf_y = [ a for a in range(y+1) ] 
    ListOf_z = [ a for a in range(z+1) ] 
   
    print([[x, y, z] for x in ListOf_x for y in ListOf_y for z in ListOf_z if x + y + z != n])
    