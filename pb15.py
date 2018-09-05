from math import factorial

'''
Fir a grid of given size, we can see that the number of paths to a certain spot
can be mapped by the numbers of Pascal's triangle
To find the number of paths through a nxn grid, we would only have to find the
number in Pascal's triangle at the 2nth row in the nth column.

We have Mahavira's formula for mapping numbers in Pascal's triangle:
(n)     n!
( )= _________
(r)  r! (n-r)!

We can substite the value of 2n for the value of n and the value of n for
since we only want to find
numbers in Pascal's triangle corresponding to square grids, we thus get the
formula for the number of paths through a nxn grid

(2n)     (2n)!
( ) =  _________
(n)     (2n!)^2

'''
def find_all_paths_for_grid(n):
    return factorial(2*n)/(pow(factorial(n),2))

print find_all_paths_for_grid(20)
