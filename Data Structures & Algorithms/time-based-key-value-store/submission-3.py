class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((timestamp, value))
        else:
            self.timemap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        my_list = self.timemap[key]
        best_time = -1
        left = 0
        right = len(my_list) - 1
        while left <= right:
            middle = (left + right) // 2
            if my_list[middle][0] <= timestamp:
                best_time = middle
                left = middle + 1
            else:
                right = middle - 1
        if best_time != -1:
            return my_list[best_time][1]
        return ""