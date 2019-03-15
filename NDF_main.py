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
		d = f.read(1)
		counter = 0
		while (d != '.'):  # This skips the numbers before the point and the point itself, so to get directly to the digits
			counter += 1
			d = f.read(1)
		testing = 1
		print("Count",counter)
		while (d != ''):
			try:
				f.seek(testing+counter)
				d = f.read(len(str(testing)))
			except ValueError:
				pass
			if d == str(testing):
				print("Found!:",d)
				g.write("Result found: {}        - {}".format(d,datetime.datetime.utcnow()))
			testing += 1
			# try:
				# if (testing%100000 == 0):
					# print("Testing",testing)
			# except Exception:
				# pass