class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        f=[1]*n
        b=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                f[i]=f[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                b[i]=b[i+1]+1
        candy=0
        for i in range(n):
            candy+=max(f[i],b[i])
        return candy
