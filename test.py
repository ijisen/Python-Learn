def my_abe(x):
    if isinstance(x, (int, float)):
        return 1
    if x < 0:
        return -x
    else:
        return x

print(my_abe(-5))
