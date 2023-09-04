"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d={}
        dummy=dum=Node(0)
        curr=head
        while curr:
            node=Node(curr.val)
            d[curr]=node
            curr=curr.next
            dum.next=node
            
            dum=dum.next
        d[None]=None
        curr=head
        while curr:
            node=d[curr]
            node.random=d[curr.random]
            curr=curr.next
        return dummy.next