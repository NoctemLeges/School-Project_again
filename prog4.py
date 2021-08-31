dt = {'West Bengal':'Kolkata','Maharastra':'Mumbai','Punjab':'chandhigar'}

l = list(dt.keys())
l.sort()

dt_sorted = {}

for i in l:
    dt_sorted[i] = dt[i]
print(dt_sorted)

