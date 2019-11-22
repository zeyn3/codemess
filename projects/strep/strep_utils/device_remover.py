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

#############################STAGE_2###########################

new_data = []
item_line_pos, block_start_pos, block_end_pos = [0,0,0]
def deactive():
    with open("../strep_slave/nodes","r") as nodes_file:
        for line in nodes_file:
            new_data.append(line)

        item_line_pos, block_start_pos, block_end_pos = [0, 0, 0]

        for i, line in enumerate(new_data):
            if receive in line:
                item_line_pos=i
                for z in range(1, 10):
                    if "set node {" in new_data[item_line_pos - z]:
                        block_start_pos = item_line_pos - z
                    if block_start_pos > 0:
                        break
                for z in range(1, 10):
                    if "}" in new_data[item_line_pos + z]:
                        block_end_pos = item_line_pos + z
                    if block_end_pos > 0:
                        break
            if block_start_pos > 0 and block_end_pos > 0:
                break

        for each in range(block_start_pos, block_end_pos+1):
            new_data[each] = f"#{new_data[each]}"

    with open("../strep_slave/nodes","w") as nodes_file:
        nodes_file.writelines(new_data)

deactive()
