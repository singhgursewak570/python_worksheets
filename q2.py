# Q2
def test_range(n):
    if (n >= 100 and n <= 1000) or n == 2000:
        return True
    else:
        return False

print(test_range(500))
print(test_range(1500))