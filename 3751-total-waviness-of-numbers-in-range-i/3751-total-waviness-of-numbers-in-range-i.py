class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        res=0
        for i in range(num1,num2+1):
            if(len(str(i))) < 3:
                res+=0
            else:
                a=str(i)
                for i in range(1,len(a)-1):
                    if int(a[i-1]) < int(a[i]) and int(a[i]) > int(a[i+1]) :
                        res+=1
                    elif int(a[i-1]) > int(a[i]) and int(a[i]) < int(a[i+1]) :
                        res+=1
        return res


        