s = input("Enter a string:")

l = s.split()
l_result = []
for i in l:
    if l.count(i)>1:
        continue
    elif l.count(i) ==1:
        l_result.append(i)
l_result.sort()

print(' '.join(l_result))