def spin_words(sentence):
    s = sentence.split(" ")
    a = []
    for i in range(len(s)):
        if len(s[i])>=5:
            a.insert(i, s[i][::-1])
        else:
            a.append(s[i])
    print(a)
    return " ".join(a)



print(spin_words("Hey fellow warriors"))

