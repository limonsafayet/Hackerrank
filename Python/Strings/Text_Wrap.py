# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

# Input Format

# The first line contains a string, S.
# The second line contains the width, w.

# Constraints
# 0 < len(S) < 100
# 0 < w < len(S)

# Output Format

# Print the text wrapped paragraph.

# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap

def wrap(string, max_width):
    output = []
    output = textwrap.fill(string, max_width)
    return output


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)