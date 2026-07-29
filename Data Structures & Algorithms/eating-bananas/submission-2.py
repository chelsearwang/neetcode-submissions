class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = 0
        for pile in piles:
            right = max(pile, right)
        while left < right:
            rate = (left+right)//2
            hours = 0
            #print(left, rate, right)
            for pile in piles:
                if pile % rate == 0:
                    hours += pile//rate
                else:
                    hours += pile//rate + 1
            if hours > h:
                left = rate + 1
            else:
                right = rate
        return right