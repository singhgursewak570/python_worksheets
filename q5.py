# Q5
def distinct_list(L):
    nl = []
    for x in L:
        if x not in nl:
            nl.append(x)
    return nl

print(distinct_list([1,2,2,3,4,4,5]))
