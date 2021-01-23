def approx(num, times):
    an, t = 1, 1
    while t < times:
        print(an)
        an = 0.5 * (an + num / an)
        t = t + 1

approx(3, 10)