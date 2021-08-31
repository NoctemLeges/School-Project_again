file = open("story.txt","r")
lines = file.readlines()
count = 0
for line in lines:
    words = line.split()
    for word in words:
        if word=="me" or word=="my":
            count+=1
file.close()
print("The number of required words is:",count)