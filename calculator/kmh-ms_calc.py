choice = int(raw_input('m/s to km/h (1) or other way around (2)'))
if (choice == 1):
	speedM = float(raw_input('Please enter the speed of the left item (m/s): '))
	print
	print str((speedM * 3600) / 1000) + 'km/h'
	print
if (choice == 2):
	speedK = float(raw_input('Please enter the speed of the left item (km/h): '))
	print
	print str((speedK / 3600) * 1000) + 'km/h'
	print
