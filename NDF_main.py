"""
Numeral Digit Finder
DESCRIPTION: This program finds a number (or numbers) inside known constants like pi, e, phi, etc where the digit-index of the number matches
the number itself, so for example the number a = 0.03451810021196314 has an 11 starting at the 11th digit

AUTHOR: Agustin Marcelo Dominguez // A.Doige [March] [2019]

LICENSE: MIT License (c) [2019] Agustin Marcelo Dominguez
		Permission, free of charge, to any person to deal in the Software without restriction, 
		including without limitation the rightsto use, copy, modify, merge, publish, distribute, and/or sublicense with the condition that
		the software is proved "as is", without warranty of any kind, express or implied.

NOTE: The massive constants were generated using the program y-cruncher (Copyright 2008-2020 by Alexander J. Yee) but in general they should be in a .txt file
on the same folder as this file. It only reads the decimals, so a period (.) should be before the digits that are to be checked
"""
import datetime
print("Running...")

constant = "pi"
with open("constant.txt",'r') as f:
	with open("results.txt",'w') as g:
		g.write("NDF Started about constant {} at {}\n".format(constant,datetime.datetime.utcnow()))
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
				g.write("{} found at {}.\n".format(testing,datetime.datetime.utcnow()))

			testing += 1

			if testing%1000000 == 0:
				print("Testing {} millones.".format(int(testing/1000000)))