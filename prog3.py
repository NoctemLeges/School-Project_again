n = int(input("Enter number of items in the dictionary:"))
dt = {}
for i in range(n):
    item = input("Enter item of dictionary:")
    dt[i+1] = item
print("Entered dictionary:",dt)
key = int(input("Enter key of the item to be deleted:"))

dt.pop(key)

print("dictionary after removal of item:",dt)
