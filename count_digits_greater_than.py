def count_digits_greater_than(n,t):
    if type(n) != int  or n < 0 or t < 0 or t > 9 or type(t) != int:
        return -1
    
    n = list(int(i) for i in str(n))
    t = int(t)
    number_greater_digits = 0
    for i in range((len(n))):
        if n[i] > t:
            number_greater_digits += 1
    
    return number_greater_digits


