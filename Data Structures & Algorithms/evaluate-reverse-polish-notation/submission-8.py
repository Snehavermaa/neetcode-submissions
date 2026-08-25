class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack=[]
        for token in tokens:
            if token!='+' and token!='-' and token!='*' and token!='/': 
                numStack.append(int(token))
            else:
                a=numStack.pop()
                b=numStack.pop()
                if token=="+":
                    r=a+b
                elif token=="-":
                    r=b-a
                elif token=="*":
                    r=a*b
                else:
                    r=int(b/a)
                numStack.append(r)
        return numStack[-1]
