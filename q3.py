# Q3
def rev_str(s):
    r = ""
    for i in range(len(s)-1, -1, -1):
        r = r + s[i]
    return r

print(rev_str("robot"))