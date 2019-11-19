# this is 2nd stage of device_remover.py and when it will finish i will merge with device remover
store = []
device = []

a = input("server:")

def func(arg):
    for i,val in enumerate(store):
        if arg in val:
            index = i
            index -= 1

            for i in store[index:]:
                i = "#" + i
                device.append(i)
                if "}" in i:
                    break
        else:
            device.append(val)





with open("../strep_slave/nodes","r") as nodes:
    for node in nodes:
        if "\n" in node:
            node = node[:-1]
        store.append(node)

func(a)
for i in device:
    print(i)
