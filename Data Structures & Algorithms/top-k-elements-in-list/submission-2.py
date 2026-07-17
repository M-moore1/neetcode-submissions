class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        sorted_items = sorted(seen.items(), key=lambda pair: pair[1], reverse=True)
        
        output = []
        for i in range(k):
            output.append(sorted_items[i][0])
        return output
