import random

def generate_matrix(rows, cols):
    return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

def sum_matrices(A, B):
    m, n = len(A), len(A[0])
    C = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

def calculate_trace(matrix):
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    return trace

def find_max(matrix):
    max_value = matrix[0][0]
    for row in matrix:
        for value in row:
            if value > max_value:
                max_value = value
    return max_value

def transpose_matrix(matrix):
    p = len(matrix)
    E = []
    for i in range(p):
        row = []
        for j in range(p):
            row.append(matrix[j][i])
        E.append(row)
    return E

def multiply_matrices(F, G):
    m, n, p = len(F), len(F[0]), len(G[0])
    H = []
    for i in range(m):
        row = []
        for j in range(p):
            value = 0
            for k in range(n):
                value += F[i][k] * G[k][j]
            row.append(value)
        H.append(row)
    return H

def main():
    m, n, p = 3, 4, 5

    A = generate_matrix(m, n)
    B = generate_matrix(m, n)
    C = sum_matrices(A, B)

    D = generate_matrix(p, p)
    trace_D = calculate_trace(D)
    max_D = find_max(D)
    E = transpose_matrix(D)

    F = generate_matrix(m, n)
    G = generate_matrix(n, p)
    H = multiply_matrices(F, G)

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

if __name__ == "__main__":
    main()