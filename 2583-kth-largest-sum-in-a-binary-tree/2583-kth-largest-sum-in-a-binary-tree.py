import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        li=[]
        q=[]
        q.append(root)
        while q:
            s=0
            l=len(q)
            for i in range(l):
                curr=q.pop(0)
                if curr:
                    s+=curr.val
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            heappush(li,-1*s)
        if len(li)<k:return -1
        for i in range(k-1):
            heappop(li)
        return -1*heappop(li)