def sum_of_cubes_even(n):
    if type(n) != int or n < 0:
        return -1
    if n > 2000:
        print("warning!!!")
   
    sum_of_cube_numbers = 0
    for i in range(0, n + 1):
        if i % 2 == 0:
            sum_of_cube_numbers += i**3
            
    return float(sum_of_cube_numbers)
