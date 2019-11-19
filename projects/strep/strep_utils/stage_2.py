store = []
device = []

a = input("server:")
index = int()

def func(arg,arg2):
    for i,val in enumerate(store):
        if arg in val:
            index = i
            index -= 1
            arg2 = index

            for i in store[index:]:
                i = "#" + i
                device.append(i)
                if "}" in i:
                    break

        else:
            device.append(val)
    device.pop(arg2)
    arg2 += 5
    device.pop(arg2)
    device.pop(arg2)
    device.pop(arg2)





with open("../strep_slave/nodes","r") as nodes:
    for node in nodes:
        store.append(node)

func(a,index)
with open("../strep_slave/nodes", "w") as nodes:
     nodes.writelines(device)
