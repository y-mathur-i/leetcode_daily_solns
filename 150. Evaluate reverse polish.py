class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        def apply_op(op, f, s):
            # print(op, f, s)
            if op == "*":
                return f*s
            if op == "/":
                # ans =  abs(f)//abs(s)
                return f/s
            if op == "-":
                return f-s
            if op == "+":
                return f+s
        for t in tokens:
            if t in ["*","-","+","/"]:
                s = stk.pop()
                f = stk.pop()
                res = int(apply_op(t, f, s))
                stk.append(res)
            else:
                stk.append(int(t))
        # print(stk)
        return stk[0]
