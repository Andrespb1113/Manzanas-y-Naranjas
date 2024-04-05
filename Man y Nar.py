def appandorgan(p1, p2, m, n, manzana, naranja):
    cant1 = 0
    cant2 = 0
    for t in manzana:
        if t + m >= p1 and t + m <= p2:
            cant1 += 1
    for x in naranja:
        if x + n >= p1 and x + n <= p2:
            cant2 += 1
    print(cant1)
    print(cant2)

appandorgan(7, 11, 5, 15, [1, 2, 3, 4, 5, 6, 8, 1000], [-4, -5, -6, -7, -8, -9, -10, -1000])
