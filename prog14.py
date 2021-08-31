d1 = eval(input("Enter a dictionary:"))
d2 = eval(input("Enter another dictionary:"))

d_result_add={}
d_result_sub={}

#Adding part
for key in d1:
    if key in d2:
        d_result_add[key] = d1[key]+d2[key]

for key in d1:
    if key not in d_result_add:
        d_result_add[key] = d1[key]
for key in d2:
    if key not in d_result_add:
        d_result_add[key] = d2[key]

print("Addition",d_result_add)

#Subbing part
for key in d1:
    if key in d2:
        d_result_sub[key] = abs(d1[key]-d2[key])

for key in d1:
    if key not in d_result_sub:
        d_result_sub[key] = d1[key]
for key in d2:
    if key not in d_result_sub:
        d_result_sub[key] = d2[key]

print("Subtraction",d_result_sub)
