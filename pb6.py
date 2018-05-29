def sumofsquares_squareofsum_difference(n):
    sum = n*(n+1)/2
    difference = pow(sum, 2)
    for i in range(1, n+1):
        difference -= pow(i,2)
    return difference

print sumofsquares_squareofsum_difference(100)
