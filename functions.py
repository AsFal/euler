def add_to_library(number, factor_library):
    for factor in factor_library:
        if factor == number:
            factor_library[factor] += 1
            break
    else:
        factor_library[number] =1
    return 
