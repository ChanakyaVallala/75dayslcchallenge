# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=[]
        queue=deque([root])
        while queue:
            s=len(queue)
            c=[]
            for nei in range(s):
                node=queue.popleft()
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        res.sort()
        m=99999999
        for i in range(len(res)-1):
            m=min(m,res[i+1]-res[i])
        return m