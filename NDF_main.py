"""
This proyect aims to find a number or numbers inside famous constants like pi,e, phi, etc, where the digit index of the number matchest
the number itself, so for example the number a = 0.03451810021196314 the number 11 is on the 11th digit

The massive constants were made using the program y-cruncher (Copyright 2008-2020 by Alexander J. Yee)

"""

constant = "pi"
import datetime
print("Running...")

with open("constant.txt",'r') as f:
	with open("results.txt",'w') as g:
		g.write("NDF Started about constant {} at {}".format(constant,datetime.datetime.utcnow()))
		candidate = f.read(1)
		while (candidate != '.'):  # This skips the numbers before the point and the point itself, so to get directly to the digits
			candidate = f.read(1)
		testing = 1
		order = 1 # Amount of digits
		current_limit = 10**order
		while candidate != '':
			if testing == current_limit:
				order += 1
				current_limit = 10**order
				candidate = candidate[1:] + f.read(2)
			else:
				candidate = candidate[1:] + f.read(1)

			if str(testing) == candidate:
				print("Found!",testing)

			testing += 1

			if testing%1000000 == 0:
				print("Testing {} millones.".format(int(testing/1000000)))