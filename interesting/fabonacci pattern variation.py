num=int(input("enter number of rows"))

p1=1
p2=0
sum=1
for i in range(1,1+num):
    for j in range(i):
        print(sum,end=" ")
        sum=p1+p2
        p2=p1
        p1=sum
    print()