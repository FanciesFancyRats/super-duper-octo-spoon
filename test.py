s = "this is a string"
for i in range(len(s)):
    if (i + 2) < len(s):
        print s[i+2]
    else:
        print s[(i+2)-len(s)]

