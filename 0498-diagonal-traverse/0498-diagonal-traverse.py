class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        row=len(mat)
        col=len(mat[0])
        s=[]
        res=[]
        for i in range(row):
            temp1=[]
            for j in range(col):
                temp1.append(0)
            s.append(temp1)
        for r in range(row):
            for c in range(col):
                if s[r][c]==0:
                    temp=[]
                    a=r
                    b=c
                    while(a<row and b>=0):
                        temp.append(mat[a][b])
                        s[a][b]=1
                        a+=1
                        b-=1
                    if (r+c) %2==0:
                        res.extend(temp[::-1])
                    else:
                        res.extend(temp)
        return res