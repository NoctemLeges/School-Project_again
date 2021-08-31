import pickle
file = open("employee.dat","rb")

received = pickle.load(file)
recv_list = list(received)
file.close()
to_remove=[]
for entry in received:
    if entry["salary"]<55000:
        to_remove.append(entry)
for entry in recv_list:
    if entry in to_remove:
        entry.clear()
        del entry
to_send = tuple(recv_list)
file = open("employee.dat","wb")

pickle.dump(to_send,file)

file.close()

file = open("employee.dat","rb")

for entry in pickle.load(file):
    if entry != dict():
        print(entry)

