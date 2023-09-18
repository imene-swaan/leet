from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = list(filter(lambda x: x != val, nums))
        return len(nums), nums

                

        


if __name__ == '__main__':
    sol = Solution()
    k, nums = sol.removeElement([0,1,2,2,3,0,4,2], 2)

    s_nums = sorted(nums[:k]) + nums[k:]
    print('k: ', k)
    print('nums: ', nums)
    print('s_nums: ', s_nums)
    
        