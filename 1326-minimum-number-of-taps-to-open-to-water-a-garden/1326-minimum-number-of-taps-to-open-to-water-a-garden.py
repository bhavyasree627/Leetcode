class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        li=[]
        for i in range(len(ranges)):
            li.append([i-ranges[i],i+ranges[i]])
        i=0
        start=0
        end=-1
        cnt=0
        li.sort()
        li.append([10**9,10**9])
        while i<len(li):
            if li[i][0]<=start:
                end=max(li[i][1],end)
                i+=1
            else:
                start=end
                cnt+=1
                if end<li[i][0] or end>=n:
                    break
        if end<n:
            return -1
        return cnt

