class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        
        # indices of bucket indicate frequency of num
        bucket = [[] for i in range(len(nums) + 1)]
        for num, count in my_dict.items():
            bucket[count].append(num)

        result = []
        count = 0
        for f in range(len(bucket)-1, 0, -1):
            if count == k:
                break
            count += len(bucket[f])
            for num in bucket[f]:
                result.append(num)
        return result


        