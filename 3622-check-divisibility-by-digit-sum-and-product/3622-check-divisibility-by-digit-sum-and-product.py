class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def sum_prod_and_sum(n):
            s = 0
            prod = 1
            while n > 0:
                d = n % 10
                prod *= d
                s += d
                n //= 10
            return s + prod
        return not (n % sum_prod_and_sum(n))
