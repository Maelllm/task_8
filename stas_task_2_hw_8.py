def maximus(a, b: int) -> int:
    c = max(a, b)
    return c


def maximus_2(k, v, i: int) -> int:
    step_1 = maximus(k, v)
    return maximus(step_1, i)


print(maximus_2(10, 14, 52))
