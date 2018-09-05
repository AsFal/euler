class Matrix:
    def __init__(self, file_name, rows):
        file = open(file_name, "r")
        text_matrix = file.read()
        self.grid=[]
        line_length = 0
        matrix_number = ""
        for i in range(0,rows):
            j=0
            self.grid.append([])
            while True:
                if text_matrix[i*line_length+j] == " ":
                    self.grid[i].append(int(matrix_number))
                    matrix_number = ""
                elif text_matrix[i*line_length+j] == "\n":
                    self.grid[i].append(int(matrix_number))
                    matrix_number = ""
                    line_length = j+1
                    break
                else:
                    matrix_number+=text_matrix[i*line_length+j]
                j+=1

    def check_horizontal_products(self,nb_of_factors):
        max_product=0
        for i in range(0,20):
            # We need to include the 16th one
            for j in range(0,21-nb_of_factors):
                product = 1
                for k in range(0,nb_of_factors):
                    product*=self.grid[i][j+k]
                if product>max_product:
                    max_product = product
        return max_product


    def check_vertical_products(self,nb_of_factors):
        max_product=0
        for i in range(0,21-nb_of_factors):
            for j in range(0,20):
                product = 1
                for k in range(0,nb_of_factors):
                    product*=self.grid[i+k][j]
                if product>max_product:
                    max_product = product
        return max_product

    def check_diagonal_products_down(self,nb_of_factors):
        max_product=0
        for i in range(0,21-nb_of_factors):
            for j in range(0,21-nb_of_factors):
                product = 1
                for k in range(0,nb_of_factors):
                    product*=self.grid[i+k][j+k]
                if product>max_product:
                    max_product = product
        return max_product

    def check_diagonal_products_up(self,nb_of_factors):
        max_product=0
        # i for row
        for i in range(nb_of_factors,20):
            for j in range(0,21-nb_of_factors):
                product = 1
                for k in range(0,nb_of_factors):
                    product*=self.grid[i-k][j+k]
                if product>max_product:
                    max_product = product
        return max_product

    def find_max_product(self):
        h = self.check_horizontal_products(4)
        v = self.check_vertical_products(4)
        dd = self.check_diagonal_products_down(4)
        du = self.check_diagonal_products_up(4)

        # Could be interesting to do this in object oriented

        if h>v and h>du and h>dd:
            return h
        elif v>du and v>dd:
            return v
        elif du > dd:
            return du
        else:
            return dd


matrix = Matrix("ressources/matrix.txt", 20)
print matrix.find_max_product()
