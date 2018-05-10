
import datetime
import csv
import calendar

def yearAptAvg(aptNumber):
	try:
		f = open("Apt" + str(aptNumber) + "_2014.csv")
	except:
		print("File not opened, none found")
		return
	csv_f = csv.reader(f)
	print(csv_f)

	sums = 0.0
	count = 0.0

	for row in csv_f:
		if (float(row[1]) > 0.0):
			sums += float(row[1])

			time = row[0].split()[1]
			if (time == "00:00:00"):
				count += 1

	#print("Average daily power consumption for : " + str(aptNumber) + " is " + str(sums/count))
	return (sums/count)
	#print(count)
	f.close()

#calculates the daily avg for any apartment given
def dayAptAvg(aptNumber, begin = 0, end = 0):
	try:
		f = open("Apt" + str(aptNumber) + "_2014.csv")
	except:
		print("File not opened, none found")
		return
	csv_f = csv.reader(f)

	#[mon,tue,wed,thu,fri,sat,sun]
	days_sum = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	days_count = [0,0,0,0,0,0,0]
	start = False

	for row in csv_f:
		date = row[0].split()[0]
		time = row[0].split()[1]
		if ((begin == 0) | (end == 0)): #default case, do the whole year
			if (float(row[1]) > 0.0):
				day = int(datetime.datetime.strptime(date,"%Y-%m-%d").weekday())
				days_sum[day] += float(row[1])
				#get the correct number of days
				if (time == "00:00:00"):
					days_count[day] += 1
		else: #due the specific region requested
			if (date == begin): #hit the start
				start = True

			if ((float(row[1]) > 0.0) & (start == True)): #do the specified region
				day = int(datetime.datetime.strptime(date,"%Y-%m-%d").weekday())
				days_sum[day] += float(row[1])
				#get the correct number of days
				if (time == "00:00:00"):
					days_count[day] += 1

			if ((date == end) & (time == "23:45:00")): #hit the end
				start = False
				break

	totals = (days_sum,days_count)
	return "day ave is " + str(totals)

def weekAptAvg(aptNumber):
	try:
		f = open("Apt" + str(aptNumber) + "_2014.csv")
	except:
		print("File not opened, none found")
		return
	csv_f = csv.reader(f)

	#[mon,tue,wed,thu,fri,sat,sun]
	week_sums = []
	start = False

	for row in csv_f:
		date = row[0].split()[0]
		time = row[0].split()[1]
		day = int(datetime.datetime.strptime(date,"%Y-%m-%d").weekday())
		if (day == 6):
			start = True
			if (time == "00:00:00"):
				week_sums.append(0.0)

		if (start == True):
			week_sums[-1] += float(row[1])


	totals = week_sums
	return "week ave is " + str(totals)

def monthAptAvg(aptNumber):
	try:
		f = open("Apt" + str(aptNumber) + "_2014.csv")
	except:
		print("File not opened, none found")
		return
	csv_f = csv.reader(f)

	month_sums = [0]
	days_count = [0]
	check = 1
	i = 0 #first index is 0, add one to get to 0

	for row in csv_f:
		date = row[0].split()[0]
		time = row[0].split()[1]
		month = int(datetime.datetime.strptime(date,"%Y-%m-%d").strftime("%m"))

		energy = float(row[1])
		if (month != check):
			month_sums.append(0.0)
			days_count.append(0.0)
			check = month
			i += 1
		else:
			month_sums[-1] += energy
			if ((time == "00:00:00") & (energy > 0.0)):
				days_count[i] += 1

	return "Month Ave of " + str(aptNumber) +" is " + str((month_sums, days_count))

def monthAptAvgSample(num):
        for num in range(1,50):
                #print (num)
                print(monthAptAvg(num))
                num += 1
        return num

def yearAptAvgSample(num):
        for num in range(1,75):
                #print (num)
                print(yearAptAvg(num))
                num += 1
        return num


#test
#print(dayAptAvg(1,"2014-12-25","2014-12-31"))
#print(dayAptAvg(5))
#print(weekAptAvg(1))
#print(monthAptAvg(43))
#print(yearAptAvg(2))
#print(monthAptAvgSample(1))
#print(yearAptAvgSample(1))
