'''Sum of Integers Up To n (integersums.py)

Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero to the input parameter.

The function should return 0 if a non-integer is passed in.'''


# consider edge cases like a non numeric value or string
# Never trust the client side input
def add(num):
    s = 0
    try:
        s = sum(range(0,num+1))
    except TypeError:
        s = 0
    print(s)
    return s

#tests
add(4)
add(-1)
add(88)