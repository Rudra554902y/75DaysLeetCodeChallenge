class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if not st:
                    return False
                elif i=='}' and st[-1]=="{":
                    st.pop()
                elif i==']' and st[-1]=="[":
                    st.pop()
                elif i==')' and st[-1]=="(":
                    st.pop()
                else:
                    return False
        return not st

            
        