from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        
        step = 0
        start = 0
        end = 0
        while end < len(nums) - 1:
            step += 1
            max_end = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= len(nums) - 1:
                    return step
                max_end = max(max_end, i + nums[i])
            start = end + 1
            end = max_end
        return step  


            


if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,1,1,4]
    print(sol.jump(nums))
    
