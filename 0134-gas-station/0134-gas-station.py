class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):return -1
        index=0
        k=0
        n=len(gas)
        for i in range(n):
            k+=gas[i]-cost[i]
            if k<0:
                index=i+1
                k=0
        return index