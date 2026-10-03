class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        mx=0
        for i in range(len(s)):
            if s[i]=="(":
                st.append(i)
            else:
                st.pop()
                if st:
                    mx=max(mx,i-st[-1])
                else:
                    st.append(i)
        return mx