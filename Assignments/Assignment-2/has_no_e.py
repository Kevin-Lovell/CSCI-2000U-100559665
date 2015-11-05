def has_no_e(line):
	if 'e' in line:
		return False
	else:
		return True


file = open("gadsby_stripped.txt")
for line in file:
	noE = has_no_e(line)
file.close()

if noE is True:
	print("There is no e in the file")
else:
	print("There is an e in the file")