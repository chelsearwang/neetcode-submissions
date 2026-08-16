class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_freq = 0 # count of most frequent task
        mydict = {}
        for task in tasks:
            if task in mydict:
                mydict[task] += 1
            else:
                mydict[task] = 1
            if mydict[task] > max_freq:
                max_freq = mydict[task]
        other_count = len(tasks) - max_freq
        num_max = 0
        for key in mydict:
            if mydict[key] == max_freq:
                num_max += 1

        gaps = (max_freq-1)*n
        print(max_freq, other_count, gaps)
        return max(len(tasks), (max_freq - 1) * (n + 1) + num_max)
