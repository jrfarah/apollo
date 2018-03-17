# this program will use past data to predict whether it will rain tomorrow or on any given day of the year
# example of the power of this wrapper

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

def getTempAndPrecip(year, month, day):
	url = "https://www.wunderground.com/history/airport/KBOS/{0}/{1}/{2}/DailyHistory.html".format(str(year), str(month), str(day))

	download_command = "wget --output-document o.html {0} && echo 'Done'".format(url)
	grep_command = "grep -A 2 '{0}' o.html"

	# download the relevant file:
	subprocess.Popen(download_command, shell=True)

	time.sleep(0.75)

	# get day of the year
	day_of_year = str(date_to_nth_day(str(year)+str(month)+str(day)))

	# print day_of_year

	# get the maximum temperature
	max_T_string = (subprocess.check_output(grep_command.format("Max Temperature"), shell=True)).split()[6]

	l = []
	for char in max_T_string:
		try:
			l.append(int(char))
		except ValueError:
			continue

	max_temp = ""
	for elem in l:
		max_temp = max_temp+str(elem)

	max_temp = float(max_temp)
	# print max_temp

	# get the minimum temperature
	min_T_string = (subprocess.check_output(grep_command.format("Min Temperature"), shell=True)).split()[6]

	l = []
	for char in min_T_string:
		try:
			l.append(int(char))
		except ValueError:
			continue

	min_temp = ""
	for elem in l:
		min_temp = min_temp+str(elem)

	min_temp = float(min_temp)
	# print min_temp

	# get the precipitation
	precip_string = (subprocess.check_output((grep_command.format("Precipitation"))+" -m 2", shell=True)).split()[12]

	l = []
	for char in precip_string:
		try:
			l.append(int(char))
		except ValueError:
			continue

	precip = ""
	for elem in l:
		precip = precip+str(elem)

	precip = float(precip)
	# print precip

	# get the maximum temperature
	humidity_string = (subprocess.check_output(grep_command.format("Average Humidity"), shell=True)).split()[3]

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

	return int(day_of_year), max_temp, min_temp, precip, humidity


automated_tests = []


filepath = "../../training_sets/humidity_set_2016_2017.csv"
names = ["Day of the year","High","low", "humidity", "Snow or not"]
dataset = pandas.read_csv(filepath, names=names)

# n = number of days you want to test
correct = 0
total = 0
n = 1
for i in range(n):
	try:
		y = random.randint(2008, 2016)
		m = random.randint(1,13)
		d = random.randint(1,28)

		# get the max, min, precip for this day
		(day, maxT, minT, p, h) = getTempAndPrecip(y,m,d)
		automated_tests.append([day, maxT, minT, h, p])

	except:
		print "Problem! continuing anyway"
		continue

for test in automated_tests:
	total += 1
	submit = test[0:4]
	if test[4] > 0:
		result = 1
	else:
		result = 0

	prediction = ClassificationNetv1.Predict(dataset, 4, submit)
	if int(prediction) == int(result):
		correct += 1
		print "correct"
		continue

# print "Total checked: ", total
# print "Total correct: ", correct
# print "Overall accuracy: ", float(correct)/float(total)

print "Checking weather for next week: "
prediction = ClassificationNetv1.Predict(dataset, 4, [80, 37, 27, 75])
print prediction