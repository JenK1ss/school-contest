def fibonachi():
    n = int(input())
    fst = 1
    scnd = 1
    i = 1
    if n == 1:
        print(0)
    else:
        while i < n - 2:
            summ = fst + scnd
            fst = scnd
            scnd = summ
            i += 1

        print(scnd)


fibonachi()
