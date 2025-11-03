def is_strictly_increasing_digits(n):
    if type(n) != int or n < 0:
        return -1
    if n<10:
        return True

    else:
        n = str(n)
        digits_list = [ i for i in n]
        for i in range((len(digits_list))-1):
            if digits_list[i] >= digits_list[i+1]:
                return False

        return True