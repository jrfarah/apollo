# this program will get important humidity data to add to the set

import sys
sys.path.insert(0, '../core/')
sys.path.insert(0, '../prep/')
sys.path.insert(0, '../training_sets/')

import pandas
import ClassificationNetv1
import subprocess
import time
import random

def date_to_nth_day(date, format='%Y%m%d'):
    date = pandas.to_datetime(date, format=format)
    new_year_day = pandas.Timestamp(year=date.year, month=1, day=1)
    return (date - new_year_day).days + 1


def getHumidity(year, month, day):
	url = "https://www.wunderground.com/history/airport/KBOS/{0}/{1}/{2}/DailyHistory.html".format(str(year), str(month), str(day))

	download_command = "wget --output-document o.html {0} && echo 'Done'".format(url)
	grep_command = "grep -A 2 '{0}' o.html"

	# download the relevant file:
	subprocess.Popen(download_command, shell=True)

	time.sleep(3)

	# get day of the year
	day_of_year = str(date_to_nth_day(str(year)+str(month)+str(day)))

	# print day_of_year

	# get the maximum temperature
	humidity_string = (subprocess.check_output(grep_command.format("Average Humidity"), shell=True)).split()[3]
	print humidity_string

	l = []
	for char in humidity_string:
		try:
			l.append(int(char))
		except ValueError:
			continue

	humidity = ""
	for elem in l:
		humidity = humidity+str(elem)

	humidity = float(humidity)
	print humidity

	

	return int(day_of_year), humidity

humidity_list = []
failed_try_list = []
for year in range(2018,2019):
	for month in range(1,):
		if month == 2:
			for day in range(1,29):
				doty, hum = getHumidity(year, month, day)


				humidity_list.append(hum)
		if month in [1,3,5,7,8,10,12]:
			for day in range(1,32):
				doty, hum = getHumidity(year, month, day)


				humidity_list.append(hum)
		if month not in [1, 2, 3,5,7,8,10,12]:
			for day in range(1,31):
				doty, hum = getHumidity(year, month, day)


				humidity_list.append(hum)

with open("humidity_list.txt", "w") as f:
	for item in humidity_list:
		print>>f, item

print "Failed: ", failed_try_list

print '============Done============'