from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)

        hindex = []
        for c in range(len(citations)):
            print(citations[c])
            count = 0
            for o in range(len(citations)):
                if citations[o] >= citations[c]:
                    count += 1
            
            if citations[c] >= count:
                hindex.append(count)
        
        return max(hindex)


if __name__ == '__main__':
    sol = Solution()
    citations = [3,0,6,1,5]
    print(sol.hIndex(citations))
