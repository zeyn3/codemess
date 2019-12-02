import os 
from datetime import datetime

source_devices_location = "/home/khazar/github/codemess/projects/strep/strep_master/devices.txt"
source_nodes_location = "/home/khazar/github/codemess/projects/strep/strep_slave/nodes"
master_devices_location = "/home/khazar/Desktop/strep/strep_master/devices.txt"
master_nodes_location = "/home/khazar/Desktop/strep/strep_slave/nodes"
slave_devices_location = "khazar@192.168.100.14:/home/khazar/strep/strep_master/devices.txt"
slave_nodes_location = "khazar@192.168.100.14:/home/khazar/strep/strep_slave/nodes"
output_source = []
output_master = []

###############################
# 1st stage
def check_and_pull(output_source,output_master,source_location,master_location,slave_location):
	with open(master_location,'r') as master:
		for line in master:
			output_master.append(line)

	with open(source_location, 'r') as source:
		for line in source:
			output_source.append(line)
	os.chdir("/home/khazar/github/codemess/")
	result_of_pull = os.popen("git pull origin dev")
	result_as_str = result_of_pull.read()
	if "Already" in result_as_str:
		print(result_as_str)
		pass
	else:
		os.system("cp {} {}".format(source_location,master_location))
		os.system("scp {} {}".format(source_location,slave_location))

##############################
#1st stage
check_and_pull(output_source,output_master,source_devices_location,master_devices_location,slave_devices_location)
check_and_pull(output_source,output_master,source_nodes_location,master_nodes_location,slave_nodes_location)

#################################
# 2nd stage

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


with open(master_devices_location,"r") as devices:
    for device in devices:
        if "\n" in device:
            device = device[:-1]
        seperate = device.split("#")
        check(seperate)

with open(master_devices_location,"w") as devices:
    devices.writelines(store)

###################################
#3rd stage

new_data = []
item_line_pos, block_start_pos, block_end_pos = [0,0,0]
def deactive():
    with open("/home/khazar/github/codemess/projects/strep/strep_slave/nodes","r") as nodes_file:
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

    with open("/home/khazar/github/codemess/projects/strep/strep_slave/nodes","w") as nodes_file:
        nodes_file.writelines(new_data)

deactive()

###################################
#4th stage

def check_if_changed(master,slave,ssh):
	master_array = []
	slave_array = []
	with open(master, "r") as file:
		for f in file:
			master_array.append(f)

	with open(slave, "r") as file:
		for f in file:
			slave_array.append(f)

	if master_array == slave_array:
		if "devices.txt" in master:
			# ssh = ssh + "strep_master/devices.txt"
			os.system("scp {} {}".format(master, ssh))
		elif "nodes" in master:
			# ssh = ssh + "strep_slave/nodes"
			os.system("scp {} {}".format(master, ssh))
		else:
			pass
	else:
		os.system("cp {} {}".format(master,slave))
		if "devices.txt" in master:
			# ssh = ssh + "strep_master/devices.txt"
			os.system("scp {} {}".format(master, ssh))
		elif "nodes" in master:
			# ssh = ssh + "strep_slave/nodes"
			os.system("scp {} {}".format(master, ssh))
		else:
			pass


check_if_changed(source_devices_location,master_devices_location,slave_devices_location)
check_if_changed(source_nodes_location,master_nodes_location,slave_nodes_location)
