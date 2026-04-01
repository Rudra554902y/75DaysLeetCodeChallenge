class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i=="+":
                val=stack.pop()
                sval=stack.pop()
                print(val+sval)
                stack.append(val+sval)
            elif i=="-":
                val=stack.pop()
                sval=stack.pop()
                print(sval-val)
                stack.append(sval-val)
            elif i=="/":
                val=stack.pop()
                sval=stack.pop()
                print(sval,val)
                stack.append(int(sval/val))
            elif i=="*":
                val=stack.pop()
                sval=stack.pop()
                print(sval*val)
                stack.append(sval*val)
            else:
                stack.append(int(i))
        return stack[-1]