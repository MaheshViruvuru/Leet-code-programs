import array


def common_prefix(lis: array):
    if len(lis) == 1:
        return lis[0]
    ele = str(min(lis, key=len))
    prefix = ''
    lis.remove(ele)
    for i in range(len(ele)):
        ans = False
        for j in lis:
            if i <= len(j) - 1:
                if len(prefix) == len(j):
                    ans = False
                    break
                elif ele[i] == j[i]:
                    ans = True
                else:
                    ans = False
                    break
        if ans:
            prefix = prefix + ele[i]
        elif not ans:
            break
    print(prefix)


Lis = ["aaa","aa","aaa"]

common_prefix(Lis)