rows = int(input("Enter the no : ")) # for entering the no
for i in range(1, rows+1): # for rows how many i how many times the loop would run
    for j in range(0,i):
        print("*", end="")
    print(" ")

row = int(input("Enter the no : ")) # for entering the no
for i in range(row , 0, -1): # for rows how many i how many times the loop would run
    for j in range(0,i):
        print("*", end="")
    print(" ")