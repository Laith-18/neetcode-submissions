class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        dictionary = {}
        results = []

        for i in nums:
            if i in dictionary:
                new_value = dictionary[i]
                new_value +=1
                dictionary.update({i:new_value})
            else:
                dictionary.update({i:1})
        
        for i in range(k):
            max_key = max(dictionary, key=dictionary.get)
            dictionary.pop(max_key)
            results.append(max_key)
        return results


        