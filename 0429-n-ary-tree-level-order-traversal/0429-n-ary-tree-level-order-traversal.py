"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res=[]
        queue=deque([root])
        while queue:
            level=[]
            for i in range(len(queue)):
                node=queue.popleft()
                level.append(node.val)
                for i in node.children:
                    queue.append(i)
            res.append(level)
        return res
        