def roman_numbers(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    summation = 0
    S = s[:]
    for i in range(len(S)):
        if i < len(s) - 1:
            if roman_dict[S[i]] >= roman_dict[S[i + 1]]:
                summation = summation + roman_dict[S[i]]
            else:
                summation = summation - roman_dict[S[i]]
        else:
            summation = summation + roman_dict[S[i]]
    print(summation)


roman_numbers("MCMXCIV")