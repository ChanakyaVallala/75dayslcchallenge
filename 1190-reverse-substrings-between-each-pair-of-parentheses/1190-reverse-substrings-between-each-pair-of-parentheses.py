class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        for ch in s:
            if ch != ')':
                st.append(ch)
            else:
                temp = []
                while st[-1] != '(':
                    temp.append(st.pop())
                st.pop()
                for c in temp:
                    st.append(c)
        return ''.join(st)
