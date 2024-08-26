a=int(input("enter no"))
for y in range(1,a+1):
    for x in range(y,a):
        print(" ",end="")
    for z in range(y):
        print("*",end="")
    print()