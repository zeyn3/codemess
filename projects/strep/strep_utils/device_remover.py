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
