Q_state = {}


def Q(n, m):
    if(n, m) in Q_state:        # 如果已经求解过该问题，不重复求解
        return Q_state[(n, m)]

    assert (n >= m)

    result = []
    if n == m:
        result = [[m]]
    else:
        r = n - m
        for k in range(1, min(r, m)+1):
            for q in Q(r, k):
                assert(max(q) <= m)
                result.append([m] + q)

    Q_state[(n, m)] = result
    return result


def solve(n):
    result = []
    for i in range(1, n+1):
        result += Q(n, i)

    return result
