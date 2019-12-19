title_name = str()

def get_title_name(field_name):
	title_raw = list()
	seperated = field_name.split("_")
	for each in seperated:
		title_raw.append(f"{each[0].upper()}{each[1:].lower()}")
	title_name = " ".join(title_raw)
	return title_name

with open("options", "r") as options:
	field_names = options.readlines()
# print(field_names)	

with open("sample_textarea.html" , "r") as sample:
	sample_content = sample.readlines()
# print(f"Sample content original:")
# for each in sample_content:
# 	print(each) 

store_for_writeliness = list()

for field_name in field_names:
	title_name = get_title_name(field_name)
	for line in sample_content:
		line = line.replace("Title",title_name.strip())
		line = line.replace("field_name",field_name.strip())
		store_for_writeliness.append(line)
# for each in store_for_writeliness:
# 	print(each) 

with open("output.html", "w") as write_to_sample:
	write_to_sample.writelines(store_for_writeliness)
