
def add_to_library(number, factor_library):
    for factor in factor_library:
        if factor == number:
            factor_library[factor] += 1
            break
    else:
        factor_library[number] =1


def lowest_common_multiple(number):
    factors = {2:1}
    # We iterate through each positive whole number smaller than the argument
    for i in range(3, number+1):
        temp = i
        # we iterate through each found factor (stored in the factors library)
        for factor in factors:
            # Verification of remainder with the module operator
            for j in range(0, factors[factor]):
                if temp%factor == 0:
                    temp = temp/factor
                else:
                    break
            # if the temp value goes to one, then all of that numbers factors are
            # in the factors library
            if temp == 1:
                break
        # at the end of the forloop, the remaining factor is added the the factor library
        else:
            add_to_library(temp, factors)
    multiple = 1
    for factor in factors:
        multiple = multiple*pow(factor, factors[factor])
    return multiple

print lowest_common_multiple(1000)
