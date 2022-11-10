""" Find the largest palindrome made from the product of two 3-digit numbers. """


def sol():
    count = 0
    i = 999
    pal = []
    while i > 99:
        j = i
        while j > 99:
            count += 1
            # print(i*j, i, j, end=" - ")
            if list(str(i * j)) == list(str(i * j))[::-1]:
                pal.append(i * j)
            j -= 1
        i -= 1

    print()
    print(count, i, j)
    return max(pal)


print(sol())
