class MedianFinder:
    arr = []

    def __init__(self):
        self.Medianfinder = []

    def addNum(self, num: int) -> None:
        k = self.arr
        k.append(num)

    def findMedian(self):
        k = self.arr
        n = len(k)
        if n % 2 == 0:
            median = (k[int(n / 2)] + k[int(n / 2) - 1]) / 2
            print(median)
        else:
            median = k[n // 2]
            print(median)
