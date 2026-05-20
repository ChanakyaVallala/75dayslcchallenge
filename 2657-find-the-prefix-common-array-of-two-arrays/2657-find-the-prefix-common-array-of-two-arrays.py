class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res=[]
        m=len(A)
        n=len(B)
        a=0
        b=0
        sa=set()
        sb=set()
        c=0
        while(a<m and b<n):
            sa.add(A[a])
            sb.add(B[b])            
            if A[a] in sb:
                c+=1
            if B[b] in sa and A[a]!=B[b]:
                c+=1
            a+=1
            b+=1
            res.append(c)
        return res