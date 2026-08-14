class Solution:
    def modifyString(self, s: str) -> str:
        temp = []
        for i in s:
            temp.append(i)
        for i in range(len(temp)):
            if temp[i] == "?":
                for j in range(26):
                    c = chr(ord("a") + j)
                    if i > 0 and temp[i-1] == c:
                        continue
                    if i < len(temp)-1 and temp[i+1] == c:
                        continue
                    temp[i] = c
                    break
        return "".join(temp)