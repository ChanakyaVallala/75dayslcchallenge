class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        temp1=[]
        temp2=[]
        temp3=[]
        temp4=[]
        for i in range(len(s1)):
            if(i%2==0):
                temp1.append(s1[i])
                temp2.append(s2[i])
            else:
                temp3.append(s1[i])
                temp4.append(s2[i])
        temp1.sort()
        temp2.sort()
        temp3.sort()
        temp4.sort()
        if(temp1==temp2 and temp3==temp4):
            return True
        return False