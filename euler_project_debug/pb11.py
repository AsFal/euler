import pdb


def convert_file_to_matrix(file_name):
    file = open(file_name, "r")
    text_matrix = file.read()
    matrix=[]
    line_length = 0
    matrix_number = ""
    for i in range(0,20):
        j=0
        matrix.append([])
        while True:
            if text_matrix[i*line_length+j] == " ":
                matrix[i].append(int(matrix_number))
                matrix_number = ""
            elif text_matrix[i*line_length+j] == "\n":
                matrix[i].append(int(matrix_number))
                matrix_number = ""
                line_length = j+1
                break
            else:
                matrix_number+=text_matrix[i*line_length+j]
            j+=1
        # matrix.append(extract_row(file_name))
    # need to find out how to read until a line (from the beginning)
    return matrix

def check_horizontal_products(matrix,nb_of_factors):
    max_product=0
    for i in range(0,20):
        for j in range(0,20-nb_of_factors):
            pdb.set_trace()
            product = 1
            for k in range(0,nb_of_factors):
                product*=matrix[i][j+k]
            if product>max_product:
                max_product = product
    return max_product


def check_vertical_products(matrix,nb_of_factors):
    max_product=0
    for i in range(0,20-nb_of_factors):
        for j in range(0,20):
            product = 1
            for k in range(0,nb_of_factors):
                product*=matrix[i+k][j]
            if product>max_product:
                max_product = product
    return max_product

def check_diagonal_products(matrix,nb_of_factors):
    max_product=0
    for i in range(0,20-nb_of_factors):
        for j in range(0,20-nb_of_factors):
            product = 1
            for k in range(0,nb_of_factors):
                product*=matrix[i+k][j+k]
            if product>max_product:
                max_product = product
    return max_product


matrix = convert_file_to_matrix("matrix.txt")
# for row in matrix:
#     print row

h = check_horizontal_products(matrix,4)
v = check_vertical_products(matrix,4)
d = check_diagonal_products(matrix,4)


if h>v and h>d:
    print h
elif v>d:
    print v
else:
    print d

##############################################################################
######################### Draft ideas ########################################
##############################################################################
# after copying the grid into a txt file

# def extract_row(string_matrix):
#     row = []
#
#     # (maybe read the whole file and check caracters)
#     # if caracter is space, next number after,
#     # if caracter is \n, than that signals a new row
#     return row[]
