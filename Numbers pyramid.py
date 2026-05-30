# n = int(input("Enter number of levels: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

# p = int(input("Enter number of levels: "))
# for q in range(1, p+1):
#     for r in range(p, q-1, -1):
#         print(r, end="")
#     print()

# a...
# az...
# azi...
# aziz💗

name = input("Enter your name: ")
for line in range(len(name)):
    for letter in range(line+1):
        print(f"{name[letter]}", end="")
    if line != len(name)-1:
        print("...")
    else:
        print("💗")