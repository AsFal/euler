def extract_numbers(file_name):
    file = open(file_name, "r")
    list_txt = file.read()
    number_list = []
    number_txt = ""
    i = 0
    string_length = len(list_txt)
    while True:
        if i+1== string_length:
            number_list.append(int(number_txt))
            number_txt = ""
            break
        elif list_txt[i] == "\n":
            number_list.append(int(number_txt))
            number_txt = ""

        else:
            number_txt += list_txt[i]
        i +=1
    return number_list

number_list = extract_numbers("ressources/hundred_50_digit.txt")

sum = 0
for number in number_list:
    sum+=number
sum//=pow(10,40)
while sum > pow(10,10):
    sum//=10
print sum
