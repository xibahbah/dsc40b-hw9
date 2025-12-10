def learn_theta(data, colors):
    max_blue = float('-inf')
    min_red = float('inf')
    for x, c in zip(data, colors):
        if c == 'blue':
            if x > max_blue:
                max_blue = x
        else:
            if x < min_red:
                min_red = x
    return 0.5 * (max_blue + min_red)


def compute_ell(data, colors, theta):
    r = 0
    b = 0
    for x, c in zip(data, colors):
        if c == 'red' and x <= theta:
            r += 1
        elif c == 'blue' and x > theta:
            b += 1
    return float(r + b)


def minimize_ell(data, colors):
    pairs = list(zip(data, colors))
    pairs.sort()
    n = len(pairs)
    pref_red = [0] * (n + 1)
    suf_blue = [0] * (n + 1)
    for i in range(n):
        pref_red[i+1] = pref_red[i] + (1 if pairs[i][1] == 'red' else 0)
    for i in range(n - 1, -1, -1):
        suf_blue[i] = suf_blue[i+1] + (1 if pairs[i][1] == 'blue' else 0)
    best_L = float('inf')
    best_theta = None
    for i in range(n):
        L = pref_red[i+1] + suf_blue[i+1]
        if L < best_L:
            best_L = L
            if i == n - 1:
                best_theta = pairs[i][0] + 1
            else:
                best_theta = 0.5 * (pairs[i][0] + pairs[i+1][0])
    return best_theta


def minimize_ell_sorted(data, colors):
    n = len(data)
    pref_red = [0] * (n + 1)
    suf_blue = [0] * (n + 1)
    for i in range(n):
        pref_red[i+1] = pref_red[i] + (1 if colors[i] == 'red' else 0)
    for i in range(n - 1, -1, -1):
        suf_blue[i] = suf_blue[i+1] + (1 if colors[i] == 'blue' else 0)
    best_L = float('inf')
    best_theta = None
    for i in range(n):
        L = pref_red[i+1] + suf_blue[i+1]
        if L < best_L:
            best_L = L
            if i == n - 1:
                best_theta = data[i] + 1
            else:
                best_theta = 0.5 * (data[i] + data[i+1])
    return best_theta
