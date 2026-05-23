# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=[]
        if not root:
            return 0
        queue=deque([root])
        while queue:
            s=len(queue)
            c=[]
            for nei in range(s):
                node=queue.popleft()
                c.append(node.val)
                if node.left:
                    if not node.left.left and not node.left.right:
                        res.append(node.left.val)
                    else:
                        queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return sum(res)
        