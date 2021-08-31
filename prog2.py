l = eval(input("Enter a list:"))

for i in range(0,len(l),2):
    if i ==len(l)-1:
        continue
    l[i],l[i+1]=l[i+1],l[i]
print(l)
    
    