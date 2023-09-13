

class Solution():
    def __init__(self):
        pass
    def twoSum(self, nums: list, target: int) -> list:
        hashmap = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in hashmap:
                return [hashmap[comp], i]
            hashmap[num] = i


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([3,2,4], 6))
