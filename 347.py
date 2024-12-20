import heapq
from collections import defaultdict
def topKFrequent(nums, k) :
    dic = defaultdict(int)
    for item in nums:
        dic[item] += 1
    hp = list(dic.keys())[:k]
    print(hp)
    print(type(hp))
    heapq.heapify(hp)
    print(hp)
    for key in list(dic.keys())[k:]:
        if dic[key] > dic[hp[0]]:
            heapq.heappop(hp)
            heapq.heappush(hp,key)
    return hp

nums = [4,1,-1,2,-1,2,3]
k = 2
topKFrequent(nums, k)
print(topKFrequent(nums, k))