class Solution:
    def checkValidString(self, s: str) -> bool:
        os=[]
        ss=[]
        for i in range(len(s)):
            if s[i]=="(":
                os.append(i)
            elif s[i]=="*":
                ss.append(i)
            else:
                if os:
                    os.pop()
                elif ss:
                    ss.pop()
                else:
                    return False
        while os and ss:
            if os.pop()>ss.pop():
                return False
        return not os