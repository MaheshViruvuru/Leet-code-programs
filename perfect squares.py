def perfect_squares(n: int):
    square = n ** 0.5
    summation = 0
    count = 0
    l = n
    if square == int(square):
        print(1)
    else:
        for i in range(n, -1, -1):
            if summation == n:
                break
            k = i ** 0.5
            if k == int(k) and i > 1:
                if n % i == 0:
                    count = int(n / i)
                    print(count)
                    return True
                elif l >= 4:
                    summation = summation + i
                    l = l - i
                    count = count + 1
        if l < 4:
            count = count + l
        print(count)


perfect_squares(19)


