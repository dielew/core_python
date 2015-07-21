#!/usr/bin/env python


def counter_year_days(start_year, end_year):
	year_days = 0
	if start_year == end_year:
		return 0
	else:
		for year in range(start_year, end_year):
			if (year % 4 == 0) or (year % 400 == 0 and year % 100 != 0):
				year_days += 366
			else:
				year_days += 365
		return year_days


def counter_month_days(start_mon, end_mon, start_day, end_day):
	last_mon_days = 0
	each_mon_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	if start_mon == end_mon:
		return end_day - start_day
	elif start_mon > end_mon:
		for mon in range(end_mon, start_mon):
			for days in range(end_day, each_mon_days[mon]):
				last_mon_days += 1
			end_day = 0
		return -(last_mon_days + start_day)
	else:
		for mon in range(start_mon, end_mon):
			for days in range(start_day, each_mon_days[mon]):
				last_mon_days += 1
			start_day = 0
		return last_mon_days + end_day


def lunaryear_adjust(start_year, end_year, month2, month1):
	if (start_year % 4 == 0) or (start_year % 400 == 0 and start_year % 100 != 0):
		if (month2 >= 3):
			return -1
		else:
			return 0
	elif (end_year % 4 == 0) or (end_year % 400 == 0 and end_year % 100 != 0):
		if (month1 >= 3): 
			return 1
		else:
			return 0
	else:
		return 0


if __name__ == '__main__':
	while True:
		date1 = raw_input('Enter the  later  date,   format should be YYYY/MM/DD:')
		date2 = raw_input('Enter the earlier date,   format should be YYYY/MM/DD:')
		y1 = int(date1[:4])
		y2 = int(date2[:4])
		m1 = int(date1[5:7])
		m2 = int(date2[5:7])
		d1 = int(date1[8:])
		d2 = int(date2[8:])
	
		if ((not(y1 % 4 == 0 or y1 % 400 == 0 and y2 % 100 != 0)) and m1 == 2 and d1 == 29) or ((not(y2 % 4 == 0 or y2 % 400 == 0 and y2 % 100 != 0)) and m2 == 2 and d2 == 29):			
			print 'Error #1: invalid date value, date Feb. 29th only exits in a lunar year!'
			break

		if y1 >= y2:
			year_days_num = counter_year_days(y2, y1)
		else:
			print 'Error #2: invalid date value, the first date should be later one!'
			break
		print 'DAYS between two dates are: %d days' %(year_days_num + counter_month_days(m2, m1, d2, d1) + lunaryear_adjust(y2, y1, m2, m1))


