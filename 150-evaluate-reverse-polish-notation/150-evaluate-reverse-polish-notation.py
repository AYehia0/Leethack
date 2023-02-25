class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Stack problem
        tokens = ["2","1","+","3","*"]
        2 -> 1 -> + pop - pop : (2 + 1)
        (2 + 1) -> 3 -> * : pop - pop : ((2 + 1) * 3) 
        """
        st = []
        ops = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in ops:
                st.append(token)
            else:
                a = int(st.pop())
                b = int(st.pop())
                if token == "+":
                    st.append(b + a)
                elif token == "-":
                    st.append(b - a)
                elif token == "*":
                    st.append(b * a)
                elif token == "/":
                    st.append(int(b / a))

                # exp = f"({b} {token} {a})"
                # st.append(exp)

        return int(st.pop())
