import math


def s_func(h, k):
    res = 0
    for r in range(1, k):
        res += (r/k) * ((h*r/k) - int(h*r/k) - 1/2)
    return res


def A_func(n, k):
    res = 0
    for h in range(k):
        if math.gcd(h, k) == 1:
            res += math.cos(math.pi * s_func(h, k) - 2 * math.pi * n * (h/k))
    return res


def ddn(n, k):
    res = math.pi * math.cosh(math.sqrt(2/3) * math.pi *
                              math.sqrt(n - 1/24)/k)/(math.sqrt(6)*k*(n-1/24))
    res = res - math.sinh(math.sqrt(2/3)*math.pi*math.sqrt(n-1/24)/k
                          )/(2*(n-1/24)*math.sqrt(n-1/24))
    return res


def partition(n):
    tmp = 0
    for k in range(1, int(math.sqrt(n))):
        tmp += A_func(n, k) * math.sqrt(k) * ddn(n, k)
    res = 1/(math.pi*math.sqrt(2)) * tmp
    return res
