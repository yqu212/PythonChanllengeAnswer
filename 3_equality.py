import re

txt = open("data.txt")
pattern = re.compile(r"[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]")
s = ""
for line in txt:
    guard = pattern.findall(line)
    for string in guard:
        s += string[4]
print(s)
