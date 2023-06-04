# Digit Cancelling Fractions


def is_valide_simplification(numerator: int, denominator: int):
    real_fract = numerator / denominator
    # print(real_fract)
    num = set(str(numerator))
    denom = set(str(denominator))

    common = num.intersection(denom)
    num = num.difference(common)
    denom = denom.difference(common)

    num = list(num)
    denom = list(denom)

    if len(num) != 1 or len(denom) != 1 or denom[0] == "0":
        return [False, num, denom]

    est_fract = int(num[0]) / int(denom[0])
    if est_fract == real_fract:
        return [True, num, denom]

    return [False, num, denom]


def main():
    works = []
    for i in range(10, 100):
        for j in range(i, 100):
            test = is_valide_simplification(i, j)

            if (i % 10 == 0 and j % 10 == 0) or (i % 11 == 0 and j % 11 == 0):
                continue

            if test[0] == True:
                # works.append([[i, j], test[1::]])
                works.append([i, j])

    return works


if __name__ == "__main__":
    # print(is_valide_simplification(49, 98))
    works = main()
    print(works)


def is_valid_simplification(numerator: int, denominator: int):
    real_fract = numerator / denominator
    num = set(str(numerator))
    denom = set(str(denominator))

    common = num.intersection(denom)
    num -= common
    denom -= common

    if len(num) != 1 or len(denom) != 1 or "0" in denom:
        return False

    est_fract = int(num.pop()) / int(denom.pop())
    return est_fract == real_fract


def main():
    works = []
    for i in range(10, 100):
        for j in range(i + 1, 100):
            if (i % 10 == 0 and j % 10 == 0) or (i % 11 == 0 and j % 11 == 0):
                continue

            if is_valid_simplification(i, j):
                works.append([i, j])

    return works


if __name__ == "__main__":
    works = main()
    print(works)
