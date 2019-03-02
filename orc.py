from collections import Counter
with open('orc.txt', 'r') as myfile:
    data = myfile.read()
sList = list(data)
print(Counter(sList))
# then i found [t, y, i, a, l, e, q, u] is rare characters with occurrence = 1 but in the wrong order
# so i found the each letter in the text file to determine the order that they appear in the mess message
# finally, i found out the result is "equality"

# cach 2
s = ''.join([line.rstrip() for line in open('orc.txt')])  # rstrip() removes all white spaces in a string
OCCURRENCES = {}
for c in s: OCCURRENCES[c] = OCCURRENCES.get(c, 0) + 1
avgOC = len(s) // len(OCCURRENCES)
print(''.join([c for c in s if OCCURRENCES[c] < avgOC]))