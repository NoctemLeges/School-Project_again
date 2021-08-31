l1 = eval(input('Enter a list:'))
l2 = eval(input('Enter another list:'))

intersection = []

for i in l1:
    if i in l2:
        intersection.append(i)
print("The intersection of the two lists is:",intersection)

union = []

for i in l1:
    union.append(i)
for i in l2:
    if i not in union:
        union.append(i)
print("The union of the two lists is:",union)
