from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-2,0,-1):
            if(nums[i]==nums[i-1] and nums[i]==nums[i+1]):
                nums.pop(i+1)
        return len(nums)

                

        


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([1,1,1,2,2,3]))
        