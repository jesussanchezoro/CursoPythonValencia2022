
def readInstance(path):
    instance = {}
    with open(path, "r") as f:
        n, p = map(int, f.readline().split())
        instance['n'] = n
        instance['p'] = p
        instance['d'] = []
        for _ in range(n):
            instance['d'].append([0] * n)
        for i in range(n):
            for j in range(i+1, n):
                u, v, d = f.readline().split()
                u = int(u)
                v = int(v)
                d = round(float(d), 2)
                instance['d'][u][v] = d
                instance['d'][v][u] = d
    return instance