from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            print('i: ', i)
            print('nums[i]: ', nums[i])
            print('last_index: ', last_index)

            if i + nums[i] >= last_index:
                last_index = i
                print('last_index: ', last_index)
        return last_index == 0


if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,1,1,4]
    print(sol.canJump(nums))
    nums = [3,2,1,0,4]
    print(sol.canJump(nums))
