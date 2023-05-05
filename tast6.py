def edit_distance(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    i, j = n, m
    operations = []
    while i > 0 or j > 0:
        if i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(('delete', s1[i - 1]))
            i -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            operations.append(('insert', s2[j - 1]))
            j -= 1
        else:
            if s1[i - 1] != s2[j - 1]:
                operations.append(('substitute', s2[j - 1]))
            i -= 1
            j -= 1
    operations.reverse()
    return dp[n][m], operations

s1 = 'abcdef'
s2 = 'azced'
distance, operations = edit_distance(s1, s2)
print(f'{distance} operations')
for operation in operations:
    print(f'{operation[0]} {operation[1]}')