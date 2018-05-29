def check_pythagorean_triplet(a,b,c):
    if a*a + b*b == c*c:
        return True
    return False

def print_triplet(a,b,c):
    print "(" + str(a) + ", " + str(b) +", " + str(c) + ")"

triplet_found = False
# because of a<b<c, the max value a can take is 332
for a in range(1, 333):
# after setting a constant value for a, we have these 2 conditions
# to connect b and c
#     b<c
#     b + c = 1000 -a
# by substituting the equation 2 into the first inequality, we get
# that
#     b<floor(1000-a/2)
    for b in range(2, (1000-a)//2 + 1):
        if check_pythagorean_triplet(a,b, (1000-a)-b):
            print a*b*(1000-a-b)
            triplet_found = True
            break
    if triplet_found:
        break
