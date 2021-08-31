story = """This is a story I am writing for the purpose of testing out this program. 
What did the '/' say to the '//'?
It said,"Tell me the decimal part" and laughed."""

file = open("story.txt","w")
file.write(story)
file.close()

count = 0
lower = 0
upper = 0
special = 0
digits = 0
file = open("story.txt","r")

lines = file.readlines()
words = []
letters = []
for line in lines:
    words.extend(line.split())

for word in words:
    count+=1
    letters.extend(list(word))
for letter in letters:
    if letter.isupper():
        upper+=1
    elif letter.islower():
        lower +=1
    elif letter.isdigit():
        digits+=1
    elif not letter.isalpha():
        special+=1
print("No of words is",count)
print("Uppercase letters are", upper)
print("lowercase letters are", lower)
print("Special characters are",special)
print("Digits are", digits)


