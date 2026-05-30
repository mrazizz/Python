# for i in range(1, 8):
#     for j in range(1, 15):
#         if (j == 8 - i) or (i == 5 and j >= 3 and j <= 10) or (j == 6 + i):
#             print("+", end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range(1, 8):
#     for j in range(1, 8):
#         if i == 1 or i == 7 or j == 8 - i:
#             print("+", end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range(1, 8):
#     for j in range(1, 8):
#         if i == 1 or j == 4 or i == 7:
#             print("+", end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range(1, 8):
#     for j in range(1, 8):
#         if i == 1 or i == 7 or j == 8 - i:
#             print("+", end="")
#         else:
#             print(" ", end="")
#     print()


for i in range(1, 8):
    for j in range(1, 8):
        if (i == 1 and j == 4) or (i == 2 and 3 <= j <= 5) or (i == 3 and (j == 2 or j == 6)) or i == 4 or (i > 4 and (j == 1 or j == 7)):
            print("+", end="")
        else:
            print(" ", end="")
            
    print(" ", end="")
    
    for j in range(1, 8):
        if i == 1 or i == 7 or j == 8 - i:
            print("+", end="")
        else:
            print(" ", end="")
            
    print(" ", end="")
    
    for j in range(1, 8):
        if i == 1 or j == 4 or i == 7:
            print("+", end="")
        else:
            print(" ", end="")
            
    print(" ", end="")
    
    for j in range(1, 8):
        if i == 1 or i == 7 or j == 8 - i:
            print("+", end="")
        else:
            print(" ", end="")
            
    print()