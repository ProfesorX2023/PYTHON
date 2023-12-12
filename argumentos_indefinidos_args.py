def factorial(*args):
    total=1
    for arg in args:
        total=total*arg

    return total

print(factorial(1,2,3,4,5,6))

