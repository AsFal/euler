file = open("big_number.txt", "r")
big_fat_number = int(file.read())



def check_first_13(number):
    multiple = 1
    temp = number
    for i in range(1,14):
        multiple *= temp%10
        temp //=10
    return multiple

# find out the last digit
# turn the big ass number into a list
nb_of_digits = 1000
highest_multiple = 0
while nb_of_digits > 13:
    multiple = check_first_13(big_fat_number)
    if multiple > highest_multiple:
        highest_multiple = multiple
    big_fat_number //=10
    nb_of_digits -= 1
print highest_multiple
