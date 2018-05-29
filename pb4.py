def check_palindrome(number):
    string_version = str(number)
    length = len(string_version)
    for i in range(0, length/2):
        if string_version[i] != string_version[length-1-i]:
            return False
    return True

def find_highest_palindrome(digits):
    i=999
    lower_bound  = 100
    highest_palindrome = 0
    first = True
    while i > lower_bound:
        for j in range(999, i-1, -1):
            multiple = i*j
            if(check_palindrome(multiple)):
                if not first:
                    lower_bound = pow(i, 2)/999
                    first = False
                if multiple > highest_palindrome:
                    highest_palindrome = multiple
                break
        i -=1
    return highest_palindrome

print find_highest_palindrome(3)
