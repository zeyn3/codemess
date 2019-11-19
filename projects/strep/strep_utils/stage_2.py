# DO NOT DELETE FOR NOW #

# # this is 2nd stage of device_remover.py and when it will finish i will merge with device remover
# store = []
# device = []

# a = input("server:")

# def func(arg):
#     for i,val in enumerate(store):
#         if arg in val:
#             index = i
#             index -= 1

#             for i in store[index:]:
#                 i = "#" + i
#                 device.append(i)
#                 if "}" in i:
#                     break
#         else:
#             device.append(val)





# with open("../strep_slave/nodes","r") as nodes:
#     for node in nodes:
#         print(f"node: {node}")  #z3
#         if "\n" in node:
#             node = node[:-1]
#             print(f"node if newline: {node}")  #z3

#         store.append(node)
#         print(f"store: {store}")  #z3

# func(a)
# for i in device:
#     print(i)


#############################################################
device_name = input("server: ")
new_data = []

with open("../strep_slave/nodes","r") as nodes_file:    
    for line in nodes_file:
        new_data.append(line)                 

    item_line_pos, block_start_pos, block_end_pos = [0, 0, 0]

    for i, line in enumerate(new_data):
        # print(f"{i}: {line}")
        if device_name in line:
            print(f"item line: {i}")
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

    print(block_start_pos, block_end_pos, item_line_pos)
    for each in range(block_start_pos, block_end_pos+1):
        new_data[each] = f"#{new_data[each]}"

    for line in new_data:
        print(line)


with open("../strep_slave/nodes","w") as nodes_file:    
    nodes_file.writelines(new_data)

          
            
