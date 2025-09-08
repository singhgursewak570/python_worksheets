# Q6
def even_list(L):
    nl = []
    for x in L:
        if x % 2 == 0:
            nl.append(x)
    return nl

print(even_list([1,2,3,4,5,6,7,8,9]))
