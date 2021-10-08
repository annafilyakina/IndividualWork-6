try:
    n = int(input("введите длину массива "))
    delta = int(input("введите delta "))
    minn = 1000
    k = 0
    a = []
    for i in range(n):
        a.append(int(input("введите элемент массива ")))
        minn = min(minn, a[i])
except ValueError as message:
    print("неверные данные")
else:

    for i in range(n):
        if (a[i] == minn + delta) or (a[i] == minn - delta):
            k += 1
    print(k)
