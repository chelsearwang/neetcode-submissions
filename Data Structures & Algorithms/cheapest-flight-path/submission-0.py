class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices[:]
            for from_, to, price in flights:
                if prices[from_] == float("inf"):
                    continue
                temp[to] = min(temp[to], prices[from_] + price)
            prices = temp

        if prices[dst] == float("inf"):
            return -1

        return prices[dst]