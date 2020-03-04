import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        result = []
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        heap = []
        heapq.heapify(heap)
        for key in hashmap.keys():
            heapq.heappush(heap, (-hashmap[key], key))
            if len(heap) > k:
                if hashmap[key] > abs(heap[0][0]):
                    heapq.heappop(heap)

        for i in range(k):
            number = heapq.heappop(heap)[1]
            result.append(number)
        return result