data_dict = {
        "Brand":{
        }
    }
    
#print(data_dict)                               # Just for testing purposes

def count():
	brand_dict = data_dict["Brand"]                 
    #outfile = open("device_data.txt", "a")
	with open("devices.txt", "r") as file_in:  
		file = file_in.readlines()             
		for line in file:                     
			res = line.strip('][').split(', ') # Converts the string "lists" into actual strings
			# list format is [brand, model]
			brand = res[0].strip('\'')            
			model = res[1].strip('\'')
			model = model.strip("\']\n")
			if brand not in brand_dict:
				brand_dict[brand] = {model.strip("\']\n"):1}
				brand_dict[brand][model] = 1
				#print("it exists" + str(data_dict))
			elif brand in brand_dict:
				if brand_dict[brand].get(model.strip("\']\n"),0) == :
					brand_dict[brand][model] = 1
				elif brand_dict[brand].get(model.strip("\']\n")) != None:
					brand_dict[brand][model] += 1
				

		file_in.close()

outfile = open("device_data.txt", "a")
count()                                      
print(data_dict, file=outfile)
print("Done")
outfile.close()
