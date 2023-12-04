from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0
            



if __name__ == '__main__':
    sol = Solution()
    citations = [3,0,6,1,5]
    print(sol.hIndex(citations))

    citations = [1,3,1]
    print(sol.hIndex(citations))

    citations = [0]
    print(sol.hIndex(citations))

    citations = [11, 10]
    print(sol.hIndex(citations))
