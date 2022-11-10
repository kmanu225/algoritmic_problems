lim = int(1e6)
Champernowne = ""
for i in range(lim):
    Champernowne += str(i)


if __name__ == "__main__":
    print(
        int(Champernowne[1])
        * int(Champernowne[10])
        * int(Champernowne[100])
        * int(Champernowne[1000])
        * int(Champernowne[10000])
        * int(Champernowne[100000])
        * int(Champernowne[1000000])
    )
