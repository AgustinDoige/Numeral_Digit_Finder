"""
Numeral Digit Finder
DESCRIPTION: This program finds a number (or numbers) inside known constants like pi, e, phi, etc where the digit-index of the number matches
the number itself, so for example the number a = 0.03451810021196314 has an 11 starting at the 11th digit

AUTHOR: Agustin Marcelo Dominguez // A.Doige [March] [2019]

LICENSE: MIT License (c) [2019] Agustin Marcelo Dominguez
		Permission, free of charge, to any person to deal in the Software without restriction, 
		including without limitation the rightsto use, copy, modify, merge, publish, distribute, and/or sublicense with the condition that
		the software is proved "as is", without warranty of any kind, express or implied.

NOTES: - The massive constants were generated using the program y-cruncher (Copyright 2008-2020 by Alexander J. Yee) but in general they should be in a .txt file
			on the same folder as this file. It only reads the decimals, so a period (.) should be before the digits that are to be checked
	   - This is not the faster version of the program. Check other branches of the repo (https://github.com/AgustinDoige/Numeral_Digit_Finder)


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