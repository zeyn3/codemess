from datetime import datetime

now = datetime.now()
time = now.strftime("%D")
receive = input("Please enter the name of device to be removed: ")
store = []

def check(arg):
    if receive in arg[0]:
        arg[1] = "deactivated on " + time + "\n"
        arg = '#'.join([arg[0],arg[1]])
        store.append(arg)
    else:
        arg[1] += "\n"
        arg = "#".join([arg[0],arg[1]])
        store.append(arg)


with open("../strep_master/devices.txt","r") as devices:
    for device in devices:
        if "\n" in device:
            device = device[:-1]
        seperate = device.split("#")
        check(seperate)

with open("../strep_master/devices.txt","w") as devices:
    devices.writelines(store)
#
#The second stage begin here
#

store2 = []
node_s = []
index = int()

def edit(arg,arg2):
    for i,v in enumerate(store2):
        if arg in v:
            index = i
            index -= 1
            arg2 = index
            for i in store2[index:]:
                i = "#" + i
                node_s.append(i)
                if "}" in i:
                    break
        else:
            node_s.append(v)
    node_s.pop(arg2)
    arg2 += 5
    node_s.pop(arg2)
    node_s.pop(arg2)
    node_s.pop(arg2)

with open("../strep_slave/nodes","r") as nodes:
    for node in nodes:
        store2.append(node)

edit(receive,index)

with open("../strep_slave/nodes","w") as nodes:
    nodes.writelines(node_s)
