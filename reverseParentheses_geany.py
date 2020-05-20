def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            inicio = i
        if s[i] == ")":
            fin = i
            a = s[:inicio]
            b = s[inicio+1:fin][::-1]
            c = s[fin+1:]
            return reverseParentheses(a + b + c)
    return s

s = "abc(cba)ab(bac)c"
print(reverseParentheses(s))
