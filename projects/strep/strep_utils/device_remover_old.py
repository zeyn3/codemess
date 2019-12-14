from datetime import datetime
import os

repo_path =  "/home/khazar/github/codemess/projects/strep/"
master_path = "/home/khazar/Desktop/STREP/master/"
slave_ssh_address_and_path = "khazar@192.168.100.16:/home/khazar/STREP/slave/"
now = datetime.now()
time = now.strftime("%D")
receive_device_name = input("Please enter the name of device to be removed: ")
store_devices_for_writelines = []
store_nodes_for_writelines = []

def deactivate_devices_and_nodes(time, receive_device_name, devices_and_nodes_path,store_devices_for_writelines,store_nodes_for_writelines):
	
	with open(f"{devices_and_nodes_path}strep_master/devices.txt", 'r') as devices:
		for device in devices:
			if "\n" in device:
				device = device[:-1]
			seperate = device.split("#")

			if receive_device_name in seperate[0]:
				seperate[1] = f"deactivated on {time}\n"
				seperate = '#'.join([seperate[0],seperate[1]])
				store_devices_for_writelines.append(seperate)
			else:
				seperate[1] = f"{seperate[1]}\n"
				seperate = '#'.join([seperate[0],seperate[1]])
				store_devices_for_writelines.append(seperate)

	with open(f"{devices_and_nodes_path}strep_master/devices.txt", 'w') as devices:
		devices.writelines(store_devices_for_writelines)

	with open(f"{devices_and_nodes_path}strep_slave/nodes", 'r') as nodes:
		for node in nodes:
			store_nodes_for_writelines.append(node)

		item_line_pos, block_start_pos, block_end_pos = [0,0,0]

		for index, line in enumerate(store_nodes_for_writelines):
			if receive_device_name in line:
				item_line_pos = index
				
				for c in range(1,10):
					if "set node {" in store_nodes_for_writelines[item_line_pos - c]:
						block_start_pos = item_line_pos - c
					if block_start_pos > 0:
						break

				for c in range(1,10):
					if "}" in store_nodes_for_writelines[item_line_pos + c]:
						block_end_pos = item_line_pos + c
					if block_end_pos > 0:
						break

			if block_start_pos > 0 and block_end_pos > 0:
				break

		for each in range(block_start_pos, block_end_pos+1):
			store_nodes_for_writelines[each] = f"#{store_nodes_for_writelines[each]}"

	with open(f"{devices_and_nodes_path}strep_slave/nodes", "w") as nodes:
		nodes.writelines(store_nodes_for_writelines)


def pull_new_data_and_complate_task(time,repo_path,deactivate_devices_and_nodes):
	os.chdir(repo_path)
	os.system("git pull origin dev")
	deactivate_devices_and_nodes(time, receive_device_name, repo_path, store_devices_for_writelines, store_nodes_for_writelines)
	os.chdir(repo_path)
	os.system(f"git add {repo_path}strep_master/devices.txt")
	os.system(f"git add {repo_path}strep_slave/nodes")
	os.system(f'git commit -m "Updated:{time}"')
	os.system("git push origin dev")
	os.system(f"cp {repo_path}/strep_master/devices.txt {master_path}")
	os.system(f"scp {repo_path}/strep_slave/nodes {slave_ssh_address_and_path}")

pull_new_data_and_complate_task(time,repo_path,deactivate_devices_and_nodes)