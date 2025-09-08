# Q1
def diff17(n):
    if n > 17:
        return 2 * abs(n - 17)
    else:
        return 17 - n

print(diff17(20))
print(diff17(10))