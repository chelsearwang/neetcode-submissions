class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        my_list = []
        for key in my_dict:
            my_list.append((key, my_dict[key]))
        sorted_list = sorted(my_list, key=lambda x: x[1], reverse=True)
        #print(sorted_list)

        result = []
        for i in range(k):
            result.append(sorted_list[i][0])
        return result
        