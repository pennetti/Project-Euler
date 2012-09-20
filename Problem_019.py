'''
Created on Jun 23, 2012

@author: PENNETTI
'''
'''
You are given the following information, but you 
may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible 
by 4, but not on a century unless it is divisible 
by 400.

How many Sundays fell on the first of the month 
during the twentieth century (1 Jan 1901 to 31 
Dec 2000)?
'''
#001    032    060    091    121    152    182    213    244    274    305    335
#001    032    061    092    122    153    183    214    245    275    306    336

def count_sun():
    num_sundays = 0
    year = 1900     
    days_in_year = 365
    day_of_week = 1 #monday
    day_of_year = 1 #jan 1
    
    #if day of year is the first of the month and day of week is sunday (7) then add to sundays
    while year < 2001:
        if year % 4 == 0 and not year % 400 == 0:
            days_in_year = 366
        while day_of_year < days_in_year:
            if (days_in_year == 365) and (day_of_year == 1 or day_of_year == 32 or day_of_year == 60  or day_of_year == 91 or day_of_year == 121 or day_of_year == 152 or day_of_year == 182 or day_of_year == 213 or day_of_year == 244 or day_of_year == 274 or day_of_year == 305 or day_of_year == 335) and (day_of_week == 7):
                num_sundays += 1
            if (days_in_year == 366) and (day_of_year == 1 or day_of_year == 32 or day_of_year == 61  or day_of_year == 92 or day_of_year == 122 or day_of_year == 153 or day_of_year == 183 or day_of_year == 214 or day_of_year == 245 or day_of_year == 275 or day_of_year == 306 or day_of_year == 336) and (day_of_week == 7):
                num_sundays += 1
            day_of_year += 1
            day_of_week += 1
            if day_of_week == 8:
                day_of_week = 1   
        day_of_year = 1 
        days_in_year = 365    
        year += 1
    return num_sundays

print (count_sun())
    