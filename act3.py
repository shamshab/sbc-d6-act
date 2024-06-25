user = int(input("Enter a number: "))

for i in range(user, 1, -1):
    print("*" * i)
for j in range(user-3):
    print("*" if j == 0 else ' ', end=" ")
for s in range(1, user+1):
    print("*" * s)
