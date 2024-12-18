#Space-Optimized LCS (For Length Only)
def lcs_space_optimized(X, Y):
    m, n = len(X), len(Y)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, [0] * (n + 1)

    return prev[n]

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS (Space Optimized):", lcs_space_optimized(X, Y))
