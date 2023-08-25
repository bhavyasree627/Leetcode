from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        c=Counter(s)
        string=""
        max_heap=[]
        for i in c.keys():
            heapq.heappush(max_heap,(-1*c[i],i))
        while len(max_heap)>=2:
            f1,h1=heapq.heappop(max_heap)
            f2,h2=heapq.heappop(max_heap)
            string+=h1
            string+=h2
            if f1+1<0:
                heapq.heappush(max_heap,(f1+1,h1))
            if f2+1<0:
                heapq.heappush(max_heap,(f2+1,h2))
        if max_heap:
            f,h=heapq.heappop(max_heap)
            if -1*f>1:
                return ""
            string+=h
        return string
            
