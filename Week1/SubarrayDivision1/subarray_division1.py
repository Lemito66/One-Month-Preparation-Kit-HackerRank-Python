def birthday(s, d, m):
    if len(s) == m:
        return 1 if sum(s) == d else 0
    return birthday(s[1:], d, m) + (1 if sum(s[0:m]) == d else 0)