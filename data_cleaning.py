from tqdm import tqdm
import os

for dirpath, dirnames, filenames in os.walk("./data"):
	for path in filenames[1:]:
		input_file = open("./data/"+path, "r")
		output_file = open("./clean_data/"+path , "w")
	
		for i, line in tqdm(enumerate(input_file)):
			if not line.startswith(("X", "Y","T", "%", 							"S","P"))  :
	         	   output_file.write(line)
            
		input_file.close()
		output_file.close()

data = ""		
for dirpath, dirnames, filenames in os.walk("./clean_data"):
	for path in filenames[1:]:
		input_file = open("./clean_data/"+path, "r")
		data += '\n' + input_file.read()
		input_file.close()

final_file = open("./clean_data/final_data.txt", "w")
final_file.write(data)


