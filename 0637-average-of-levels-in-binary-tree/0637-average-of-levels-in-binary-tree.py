# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res=[]
        queue=deque([root])
        while(queue):
            l=len(queue)
            c=[]
            for i in range(l):
                node=queue.popleft()
                c.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(sum(c)/(len(c)))
        return res
        