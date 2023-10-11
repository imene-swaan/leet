from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicate_count = 0
        for i in range(1, len(nums)):
            print('nums: ', nums)
            if nums[i] == nums[i-1]:
                print('duplicate: ', nums[i], ' at index: ', i)
                duplicate_count += 1
            
            else:
                print('not duplicate: ', nums[i], ' at index: ', i)
                nums[(i-duplicate_count)] = nums[i]
                print('new nums: ', nums)

        return len(nums) - duplicate_count, nums

                

        


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([1,1,1,2,2,3]))
        