inp=int(input("enter no"))
# print(" "* (a-1), "1")
# for y in range(1,a):
#     ini=1
#     for x in range(y,a):
#         print(" ",end="")
#     for z in range(1,y+1):
#         ini=ini+2
#     for f in range(ini,0,-2):
#         print(f ,end="")
        
#     print()
a=1
b=1
for y in range(1,inp+1):
    a=b
    b+=2
    for x in range(y,inp):
        print(" ",end="")
    for z in range(y):
        print(a,end="")
        a-=2
    print()


 