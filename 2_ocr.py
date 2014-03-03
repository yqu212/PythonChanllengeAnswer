# f = open("d:\desktop\data.txt")
# a_dict = {}
# for line in f:
    # for c in line:
        # if a_dict.has_key(c):
            # a_dict[c] += 1
        # else:
            # a_dict[c] = 1

# print(a_dict)

f = open("d:\desktop\data.txt")
a_dict = ""
for line in f:
    for c in line:
        if c.isalpha():
            a_dict += c

print(a_dict)
