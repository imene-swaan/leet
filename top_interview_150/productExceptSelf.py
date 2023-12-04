from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
            right[n-i-1] = right[n-i] * nums[n-i]
        return [left[i] * right[i] for i in range(n)]
        


if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))

    nums = [-1,1,0,-3,3]
    print(Solution().productExceptSelf(nums))
