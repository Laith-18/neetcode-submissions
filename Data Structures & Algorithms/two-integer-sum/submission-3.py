class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        for index,number in enumerate(nums):
            wanted = target - number

            if wanted in nums:
                if index != nums.index(wanted):
                    index2= nums.index(wanted)
                    if index>index2:
                        return[index2,index]
                    else:
                        return[index,index2]
        return None
                   