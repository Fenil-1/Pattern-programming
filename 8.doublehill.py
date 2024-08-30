a=int(input("enter no"))
for y in range(1,a+1):
    for x in range(y,a):
        print(" ",end="")
    for z in range(y):
        print("*",end="")
    for i in range(1,y):
        print("*",end="")
    for j in range(y,a):
        print(" ",end="")
    for k in range(y,a):
        print(" ",end="")
    for l in range(y):
        print("*",end="")
    for m in range(1,y):
        print("*",end="")

    print()