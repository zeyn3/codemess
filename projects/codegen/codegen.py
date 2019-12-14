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

with open("sample.html" , "r") as sample:
	sample_content = sample.readlines()

store_for_writeliness = list()

for field_name in field_names:
	title_name = get_title_name(field_name)
	for line in sample_content:
		line = line.replace("Title",title_name)
		line = line.replace("field_name",field_name)
		store_for_writeliness.append(line)

with open("output.html", "r") as write_to_sample:
	write_to_sample.writelines(store_for_writeliness)
