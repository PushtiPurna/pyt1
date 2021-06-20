lists = []
for i in range(int(input())):
    s = input().split()
    for i in range(1,len(s)):
        s[i] = int(s[i])
        
    if s[0] == "append":
        lists.append(s[1])
    elif s[0] == "insert":
        lists.insert(s[1],s[2])
    elif s[0] == "remove":
        lists.remove(s[1])
    elif s[0] == "pop":
        lists.pop()
    elif s[0] == "sort":
        lists.sort()
    elif s[0] == "reverse":
        lists.reverse()
    elif s[0] == "print":
        print (lists)