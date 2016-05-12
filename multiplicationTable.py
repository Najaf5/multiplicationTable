def multiplicationTable(smaller, larger):
	''' Returns a multiplication table containing all the products between the smaller and larger numbers inputed by the user.  '''
	
	table = []
	output = "  "
	
	for j in range(smaller, larger + 1):
		row = [str(j) + "|"]
		output += "   " + str(j)
	
		for i in range(smaller, larger + 1):
			currentProduct = i * j
			row.append(currentProduct)
			
		table.append(row)
	output += "\n   ---------------\n"
	
	for item in table:
		for z in item:
			output += " {} ".format(z)
		output += "\n"
	
	return(output)
	
#----------MAIN PROGRAM----------

smaller = int(input("Tell me a starting number: "))
larger = int(input("Tell me an ending number: "))
print(multiplicationTable(smaller, larger))