def reverseWords(s: str):
    lis = s.split(" ")
    print(lis)
    arr = []
    for ele in lis:
        if ele.strip():
            arr.append(ele)
    string = ''
    lis2 = arr[:: -1]
    for i in range(len(lis2)):
        if i == len(lis2) - 1:
            string = string + lis2[i]
        elif i < len(lis2) - 1:
            string = string + lis2[i] + ' '
    print(string)


reverseWords("the sky is blue")