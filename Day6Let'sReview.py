# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for i in range(0, t):
    word = str(raw_input())
    even = ""
    odd = ""        
    for i in range(len(word)):
        if i %2 == 0:
            even += word[i]
        else:
            odd += word[i]
    print(str(even) + " " + str(odd))
