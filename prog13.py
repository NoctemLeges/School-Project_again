str = input("Enter a string:")
str = str.upper()
characters = []
vowels = 0
consonants = 0;
frequency = {}
for c in str:
    characters.append(c)
for c in characters:
    frequency[c] = characters.count(c)
    if c in "aeiouAEIOU":
        vowels +=1
    if c not in "aeiouAEIOU" and c.isalpha():
        consonants+=1
for key in frequency:
    print(key ,'\t',"-","\t",frequency[key])
print("Number of vowels=",vowels)
print("Number of consonants=",consonants)
