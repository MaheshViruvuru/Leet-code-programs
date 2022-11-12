class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        if x < 0:
            k = -x
            while (k > 0):
                remainder = k % 10
                reverse = reverse * 10 + remainder
                k = k // 10
            reverse = -reverse
        else:
            while (x > 0):
                remainder = x % 10
                reverse = reverse * 10 + remainder
                x = x // 10

        if pow(2, 31) - 1 >= reverse >= -pow(2, 31):
            return reverse
        else:
            return 0