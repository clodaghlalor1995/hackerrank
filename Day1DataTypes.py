i = 4
d = 4.0
s = 'HackerRank '
contents = []
while True:
    try:
        line = raw_input()
    except EOFError:
        break
    contents.append(line)
print(int(contents[0])+i)
print(float(contents[1])+d)
print(s + contents[2])
