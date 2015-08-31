item1 = float(raw_input('Please enter the speed of item 1 moving right from 0 (m/s): '))
item2 = float(raw_input('Please enter the speed of item 2 left towards 0 (m/s): '))
distance1 = float(raw_input('Please enter the distance of item 1 from 0 (m): '))
distance2 = float(raw_input('Please enter the distance of item 2 from 0 (m): '))
time1 = float(raw_input('Item 1 time delay (s): '))
time2 = float(raw_input('Item 2 time delay (s): '))
print 'Equasion: ' + str(item1) + '(x+(' + str(-(time1)) + ')) + (' + str(-(distance1)) + ') = ' + str(-(item2)) + '(x+(' + str(time2) + ')) + (' + str(distance2) + ')'
