# Given the names and grades for each student in a class of N students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example
# records = [["chi",20.0],["beta",50.0],["alpha",50.0]]
# The ordered list of scores is [20.0,50.], so the second lowest score is 50.0. There are two students with that score: 
# ["beta","alpha"]. Ordered alphabetically, the names are printed as:

# alpha
# beta
# Input Format

# The first line contains an integer, N, the number of students.
# The 2N subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints

# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. 
# If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are 5 students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, 
# so we order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([score,name])
    
    # Sort list in Ascending order
    student.sort()
   
    # Assign the first score to a list which will be the minimum
    grade = student[0][0]
    
    # Loop through the list by excluding first item in the list and find the second lowest
    for i in range(1,len(student)):
        if grade < student[i][0]:
            grade = student[i][0]
            break
    
    # Loop through the list and print names based on the second lowest score
    for i in range(1,len(student)):
        if student[i][0] == grade:
            print(student[i][1])