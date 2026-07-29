class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key is tuple of frequencies, value is list of anagrams
        my_dict = {}

        # get list index based on alphabet letter
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alpha_dict = {}
        for i in range(len(alphabet)):
            alpha_dict[alphabet[i]] = i
        """
        
        for word in strs:
            my_list = [0] * 26  # stores frequency of each letter in word
            for char in word:
                my_list[ord(char) - ord('a')] += 1  # use ascii vals
            my_tuple = tuple(my_list)   # convert to tuple to use as key
            if my_tuple in my_dict:
                my_dict[my_tuple].append(word)
            else:
                my_dict[my_tuple] = [word]
        
        result = []
        for key in my_dict:
            result.append(my_dict[key])
        return result