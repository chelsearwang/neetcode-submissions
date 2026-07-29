class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alpha_dict = {}
        for i in range(len(alphabet)):
            alpha_dict[alphabet[i]] = i
        
        for word in strs:
            my_list = [0] * 26
            for char in word:
                my_list[alpha_dict[char]] += 1
            my_tuple = tuple(my_list)
            if my_tuple in my_dict:
                my_dict[my_tuple].append(word)
            else:
                my_dict[my_tuple] = [word]
        
        result = []
        for key in my_dict:
            result.append(my_dict[key])
        return result