# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap=[]
        def traversal(root):
            if not root:
                return 
            traversal(root.left)
            heap.append(root.val)
            traversal(root.right)
        traversal(root)
        print(heap)
        return heap[k-1]