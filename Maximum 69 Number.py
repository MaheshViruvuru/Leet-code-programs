class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        if str_num.count("9") == len(str_num):
            return num
        else:
            arr = []
            for i in range(len(str_num)):
                str_dupl = str_num[:]
                k = None
                if str_dupl[i] == "9":
                    k = str_dupl.replace(str_dupl[i], "6", 1)
                elif str_dupl[i] == "6":
                    k = str_dupl.replace(str_dupl[i], "9", 1)
                arr.append(int(k))
            arr.sort()
            return arr[-1]