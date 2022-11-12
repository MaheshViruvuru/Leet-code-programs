class StockSpanner:

    def __init__(self):
        self.Stackspanner = []

    def next(self, price: int) -> int:
        out_put = 1
        while self.Stackspanner and self.Stackspanner[-1][0] <= price:
            out_put = out_put + self.Stackspanner.pop()[1]

        self.Stackspanner.append([price, out_put])
        return out_put

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# sample input

# Input
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]
# Output
# [null, 1, 1, 1, 2, 1, 4, 6]
