class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        results = []
        nums.sort()

        for i in range(len(nums)):

            target = int(nums[i]) * -1

            left,right = i+1,len(nums)-1


            while left < right:

                selected = nums[left] + nums[right]

                if selected == target:
                    var = [nums[i], nums[left], nums[right]]
                    if var in results:
                        pass
                    else:
                        results.append(var)
                    left += 1
                    right -= 1
                
                elif selected < target:
                    left+=1
            
                else:
                    right-=1

        return results