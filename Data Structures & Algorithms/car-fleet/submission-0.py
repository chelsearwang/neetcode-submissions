class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(position)):
            p = position[i]
            s = speed[i]
            t = (target-p) / s   # float or int division?
            time.append(t)
        cars = sorted(zip(position, time))
        # print(cars)
        fleets = 0
        largest_time = 0
        for car in reversed(cars):
            if car[1] > largest_time:
                fleets += 1
                largest_time = car[1]
        return fleets