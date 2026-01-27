Rownum= 5
space = Rownum - 1

for i in range (1,Rownum + 1):
    for j in range (1, space + 1):
        print(end=" ")
    space = space -1

    for j in range (2 * i - 1):
        print( end = "*")
    print()
space = 1

for i in range(1 , Rownum):
    for j in range (1, space + 1):
        print(end = " ")
    space = space + 1 
    for j in range (1 ,2*(Rownum - i)):
        print(end= "*")
    print()