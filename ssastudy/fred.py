import re
re_fred = re.compile("(.*)(Fred)(.*)")
s = "My friend Fred likes Jill."
m = re_fred.search(s)
print(m.group(1))
