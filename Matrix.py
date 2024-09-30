import random

# Step 1: Generate random integer matrix A and B of dimension mxn
m = 3  # Rows
n = 4  # Columns
A = [[random.randint(1, 10) for _ in range(n)] for _ in range(m)]
B = [[random.randint(1, 10) for _ in range(n)] for _ in range(m)]

# Step 2: Calculate the sum in another matrix C
C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
    C.append(row)

# Step 3: Generate random integer matrix D of dimension pxp
p = 5
D = [[random.randint(1, 10) for _ in range(p)] for _ in range(p)]

# Step 4: Calculate the trace of D (sum of diagonal elements)
trace_D = 0
for i in range(p):
    trace_D += D[i][i]

# Step 5: Calculate the maximum value in matrix D
max_D = D[0][0]
for row in D:
    for value in row:
        if value > max_D:
            max_D = value

# Step 6: Calculate the transpose of D in another matrix E
E = []
for i in range(p):
    row = []
    for j in range(p):
        row.append(D[j][i])
    E.append(row)

# Step 7: Generate random integer matrix F (mxn) and G (nxp)
F = [[random.randint(1, 10) for _ in range(n)] for _ in range(m)]
G = [[random.randint(1, 10) for _ in range(p)] for _ in range(n)]

# Step 8: Calculate the multiplication of F and G in another matrix H
H = []
for i in range(m):
    row = []
    for j in range(p):
        value = 0
        for k in range(n):
            value += F[i][k] * G[k][j]
        row.append(value)
    H.append(row)

# Output all results
print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nMatrix C (A + B):")
for row in C:
    print(row)

print("\nMatrix D:")
for row in D:
    print(row)

print("\nTrace of Matrix D:", trace_D)
print("Maximum value in Matrix D:", max_D)

print("\nTranspose of Matrix D (E):")
for row in E:
    print(row)

print("\nMatrix F:")
for row in F:
    print(row)

print("\nMatrix G:")
for row in G:
    print(row)

print("\nMatrix H (F * G):")
for row in H:
    print(row)
