from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        n = len(nums)
        print(n//2)
        return nums[n//2]

        



if __name__ == '__main__':
    sol = Solution()
    nums = [3,2,3]
    print(sol.majorityElement(nums))
