def ugly_number(n: int):
    fact_lis = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            fact_lis.append(i)
    print(fact_lis, len(fact_lis))
    lim_primes = [2, 3, 5]
    count = 0
    for i in fact_lis:
        if i in lim_primes:
            print(i)
            count += 1
    print(count)
    if count == len(fact_lis):
        print("true")
    else:
        print("false")


ugly_number(14)