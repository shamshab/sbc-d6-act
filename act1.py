rows = int(input("Column: "))
column = int(input("Row: "))
i = 1
j = 1
while i <= rows:
    while j <= column:
        if i == 1 or j == 1 or i == rows or j== column:
           print("*", end="")
        else:
           print(" ", end="")
        j += 1 
    j = 1
    print(" ")
    i += 1  
