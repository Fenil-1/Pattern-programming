
def cap_f():
    for i in range(5):
        for j in range(5):
            if j==0:
                print("f",end="")
            elif i==0 or i==2:
                print("f",end="")
        print()      
def cap_e():
    for i in range(5):
        for j in range(5):
            if j==0:
                print("e",end="")
            elif i==0 or i==2 or i==4:
                print("e",end="")
        print()
def cap_n():
    dec=4
    for i in range(5):
        for j in range(1):
            print("n",end="")
        for k in range(1):
            print(" "*i,end="")
        for l in range(1):
            print("n",end="")
        for m in range(1):
            print(" "*dec,end="")
            dec-=1
        for n in range(1):
            print("n",end="")
        print()
def cap_i():
    for i in range(5):
        for j in range(5):
            if i==0 or i==4:
                print("i",end="")
            elif j==0 or j==1:
                print(" ",end="")
            elif j==2:
                print("i",end="")
        print()
def cap_l():
    
    for i in range(5):
        for j in range(5):
            if j==0:
                print("l",end="")
            elif i==4:
                print("l",end="")
        print()


def print_fenil():
    cap_f()
    cap_e()
    cap_n()
    cap_i()
    cap_l()

print_fenil()