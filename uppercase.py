 #!/usr/bin/env python3
def uppercase(s):
    uppercase_str = ""
    for c in s:
        if ord(c)>= 97 and ord(c) <= 122:
            uppercase_str += chr(ord(c) - 32)
        else:
            uppercase_str += c
    print("{}\n". format(uppercase_str))
uppercase("hello, world")
    