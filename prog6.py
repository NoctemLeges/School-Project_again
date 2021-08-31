file = open("hello.txt",'r')
count = 0
lines = file.readlines()

for line in lines:
    words = line.split()
    for word in words:
        if len(word) == 3:
            count+=1
file.close()

print("The number of three letter words are:",count)