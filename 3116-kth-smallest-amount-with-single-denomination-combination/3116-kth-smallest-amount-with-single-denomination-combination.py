from math import gcd
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        def lcm(a, b):
            return a // gcd(a, b) * b
        
        def count(x):
            total = 0
            for mask in range(1, 1 << n):
                current_lcm = 1
                bits = 0
                valid = True
                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        current_lcm = lcm(current_lcm, coins[i])
                        if current_lcm > x:
                            valid = False
                            break
                if not valid:
                    continue
                amount = x // current_lcm
                if bits % 2 == 1:
                    total += amount
                else:
                    total -= amount
            return total
        
        left = 1
        right = min(coins) * k
        while left < right:
            mid = left + (right - left) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
