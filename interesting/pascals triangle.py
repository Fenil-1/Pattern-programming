num=int(input("Enter number of rows : "))
list=[]

for i in range(num):
    temp_list=[]
    for j in range(i+1):
        if j==0 or i==j:
            temp_list.append(1)
        else:
            temp_list.append(list[i-1][j-1]+list[i-1][j])
    print(temp_list)
    list.append(temp_list)     


