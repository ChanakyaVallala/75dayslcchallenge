class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        temp=[]
        for i in strs:
            k="".join(sorted(i))
            if k not in d:
                d[k]=[]
            d[k].append(i)
        res=[]
        for key,val in d.items():
            res.append(val)
        return res