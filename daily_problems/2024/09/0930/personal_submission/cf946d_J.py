def main():
    n, m, k = map(int, input().split())
    f = [[inf] * (k + 1) for _ in range(n + 1)]
    for j in range(k+1):
        f[0][j] = 0

    for i in range(n):
        s = input()
        idx = [i for i in range(m) if s[i] == '1']
        d = len(idx)

    # if d > 0:
        stay = [inf] * (d + 1)
        stay[0] = 0

        for j in range(d):
            for jj in range(j, d):
                stay[jj-j+1] = min(stay[jj-j+1], idx[jj] - idx[j] + 1)

        for j in range(k+1):
            for x in range(d+1):
                if x > j: break
            # for x in range(min(j, d) + 1):
                f[i+1][j] = min(f[i][j-x] + stay[d-x], f[i+1][j])

    print(f[n][k])
