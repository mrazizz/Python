a = [[1, 2],
           [3, 4]]

b = [[5, 6],
           [7, 8]]

# a = [[00, 01],
#      [10, 11]]
# b = [[00, 01],
#      [10, 11]]

# a[0][0]*b[0][0] + a[0][1]*b[1][0] || a[0][0]*b[0][1] + a[0][1]*b[1][1]
# a[1][0]*b[0][0] + a[1][1]*b[1][0] || a[1][0]*b[0][1] + a[1][1]*b[1][1]

def matrix_multiply(a, b):
    c = []
    for i in range(len(a)):
        c.append([])
        for j in range(len(b[0])):
            c[i].append(0)

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]

    for row in c:
        print(row)

if len(a[0]) != len(b):
    print("The matrices cannot be multiplied because number of columns of first matrix is not equal to rows of second matrix.")
    exit()
else:
    matrix_multiply(a, b)