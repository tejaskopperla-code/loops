rows = int(input("enter the amout of rows that your mirrored right angle triangle supposed to have :   " ))
for i in range(1 , rows + 1):
    for j in range(rows - i):
        print(" ", end ="")
    for k in range(2 * i - 1):
        print("*", end ="")
    print()