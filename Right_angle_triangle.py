print("Half pyramid pattern with stars (*)")
n = int(input("enter the number of rows that you want to print the pattern:   "))

for i in range(n):
    for j in range(i + 1 ):
        print("*",end ="")
    print()
