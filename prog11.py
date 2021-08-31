l = [1,2,3,4,5,6,7,8,9,4,5,3,7,7]
l.sort()
duplicate=[]
frequency={}
print("The second maximum number is:",l[-2])
for i in l:
    if l.count(i) >1 and i not in duplicate:
        duplicate.append(i)
    frequency[i] = l.count(i)
print("The duplicate elements are:",duplicate)
freq_list = list(frequency.values())
freq_list.sort()
f_max = freq_list[-1]

for key in frequency:
    if frequency[key] ==f_max:
        print("highest frequency number:",key)