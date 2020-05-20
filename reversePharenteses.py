
"""
def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            print("s[:start]=", s[:start], "[start+1:end][::-1]=", s[start+1:end][::-1],"s[end+1:]=", s[end+1:], "Todos juntos= ", s[:start] + s[start+1:end][::-1] + s[end+1:])
            return reverseParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s
"""

def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            inicio = i
        if s[i] == ")":
            fin = i
            a = s[inicio:]
            b = s[inicio:fin][::-1]
            c = s[fin:]
            reverseParentheses(a + b + c)

s = "abc(cba)ab(bac)c"
print(reverseParentheses(s))

# 1 return "apmnolkjihgfedcbq"
# 2 s: "co(de(fight)s)"
# 2 return "cosfighted"
# 3 s: ""abc(cba)ab(bac)c"
# 3 return "abcabcabcabc"
# 4 s: "The ((quick (brown) (fox) jumps over the lazy) dog)"
# 4 return "The god quick nworb xof jumps over the lazy"
"""
    l = []
    c = 0
    sw = 0
    for i in range(len(s)):
        if s[i] == "(":
            c = i
            while c != len(s):
                print("Caracter: ", s[c], "Parentesis (: ", sw)
                if s[c] != ")" and sw == 0:
                    l.append(s[c])
                elif s[c] == "(" and sw > 0:
                    sw -= 1
                elif s[c] == "(" and c != i:
                    sw += 1
                c += 1
"""