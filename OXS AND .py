def xo(s):
    s = s.lower()
    a = s.count("x")
    b = s.count("o")
    print(a)
    print(b)
    return a==b


print(xo("oooXEoXXoooXoCXoXXXoXoXXAooXXdXoboXoXXoXoooooXXoXXXoooXXoXXoXoX"))