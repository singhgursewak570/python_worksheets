n=int(input("ENTER THE NUMBER \n"))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
    else:
        None
if flag==0:
    print("IT IS PRIME")
else:
    print("IT IS NOT PRIME")