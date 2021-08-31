import pickle

file = open("employee.dat","wb")

entries=(
    {"empid":1,"name":"Manoj","salary":50000,"age":30},
    {"empid":2,"name":"Tanmay","salary":70000,"age":34},
    {"empid":3,"name":"Alia","salary":75000,"age":32},
    {"empid":4,"name":"Yuva","salary":50000,"age":40},
    {"empid":5,"name":"Monica","salary":80000,"age":43}
)
pickle.dump(entries,file)

file.close()

file = open("employee.dat","rb")

received = pickle.load(file)

for entry in received:
    name_recv=entry["name"]
    if name_recv[0]=="M":
        print(entry)