class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        listOfList = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            
            search = -val
            j = i+1
            k = len(nums)-1

            while j < k:
                s = nums[j] + nums[k]
                if s == search:
                    listOfList.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
                elif s < search:
                    j += 1
                else: 
                    k -= 1

        return listOfList
