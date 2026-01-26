string = input(" please enter your own word :  ")
char = input("please enter your own charcter from the word that you wrote to check the ocurrance :  ")

i = 0
count = 0

while( i < len(string)):

    if (string[i] == char):
        count = count + 1 
    i = i + 1 


print(" the total number of time the charcter", char," has ocurred in this word is :  ", count)
