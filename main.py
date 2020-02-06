# Michael Carnall - Started 5/12/2019

# Let's try and make Counter till the end of term

# Ideas (Read: Let's make it unnecessarily complicated)
# Store term dates in file, say spreadsheet, and pull from there? (allowing for easy changing each year by staff) - Done (NOW RETURNING MONTHS AS A NUMERICAL VALUE! HOORAY!)
# When not a term, state when the next term starts?
# State how many days before end of last term?

# For getting current date:
import datetime
current = datetime.datetime.now(datetime.timezone.utc)
today = datetime.date.today()
year = current.year
month = current.month
day = current.day
hour = current.hour
minute = current.minute
second = current.second
# import module for reading the spreadsheet:
import xlrd
workbook = xlrd.open_workbook(r'Term Dates.xlsx')
worksheet = workbook.sheet_by_name('Term Dates')

# Find way to convert month to number from 1-12 - list.index() function:
monthlist = ["Don't want index() returning 0 so here's a placeholder", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Variable from denoting if term or break (and which) - I have a hunch I'll need these later:
term = 0
notterm = 0

# Current year's terms (pulled from excel file using xlrd module):
# Term 1:
t1daystart = worksheet.cell(2, 1).value
t1monthstart = monthlist.index(worksheet.cell(2,2).value)
t1yearstart = worksheet.cell(2, 3).value
t1dayend = worksheet.cell(2, 4).value
t1monthend = monthlist.index(worksheet.cell(2,5).value)
t1yearend = worksheet.cell(2, 6).value
# Term 2:
t2daystart = worksheet.cell(3, 1).value
t2monthstart = monthlist.index(worksheet.cell(3,2).value)
t2yearstart = worksheet.cell(3, 3).value
t2dayend = worksheet.cell(3, 4).value
t2monthend = monthlist.index(worksheet.cell(3,5).value)
t2yearend = worksheet.cell(3, 6).value
# Term 3:
t3daystart = worksheet.cell(4, 1).value
t3monthstart = monthlist.index(worksheet.cell(4,2).value)
t3yearstart = worksheet.cell(4, 3).value
t3dayend = worksheet.cell(4, 4).value
t3monthend = monthlist.index(worksheet.cell(4,5).value)
t3yearend = worksheet.cell(4, 6).value
# Term 4:
t4daystart = worksheet.cell(5, 1).value
t4monthstart = monthlist.index(worksheet.cell(5,2).value)
t4yearstart = worksheet.cell(5, 3).value
t4dayend = worksheet.cell(5, 4).value
t4monthend = monthlist.index(worksheet.cell(5,5).value)
t4yearend = worksheet.cell(5, 6).value
# Term 5:
t5daystart = worksheet.cell(6, 1).value
t5monthstart = monthlist.index(worksheet.cell(6,2).value)
t5yearstart = worksheet.cell(6, 3).value
t5dayend = worksheet.cell(6, 4).value
t5monthend = monthlist.index(worksheet.cell(6,5).value)
t5yearend = worksheet.cell(6, 6).value
# Term 6:
t6daystart = worksheet.cell(7, 1).value
t6monthstart = monthlist.index(worksheet.cell(7,2).value)
t6yearstart = worksheet.cell(7, 3).value
t6dayend = worksheet.cell(7, 4).value
t6monthend = monthlist.index(worksheet.cell(7,5).value)
t6yearend = worksheet.cell(7, 6).value

# Stating who made it and when
print("Written by Michael Carnall: 5/12/2019 - 21/1/2020\n")

# State current time and date:
print("The time is " + str(hour) + ":" + str(minute) + ":" + str(second) +
" UTC on " + str(day) + "/" + str(month) + "/" + str(year))

# Compare if current day, month and year are within term start and end dates:
if (t1daystart <= day and t1monthstart == month and t1yearstart == year) or (day <= t1dayend and month == t1monthend and year == t1yearend):       # Term 1
    term = 1
    print("It is currently the 1st term")
elif (t2daystart <= day and t2monthstart == month and t2yearstart == year) or (day <= t2dayend and month == t2monthend and year == t2yearend):    # Term 2
    term = 2
    print("It is currently the 2nd term")
elif (t3daystart <= day and t3monthstart == month and t3yearstart == year) or (day <= t3dayend and month == t3monthend and year == t3yearend):    # Term 3
    term = 3
    print("It is currently the 3rd term")
elif (t4daystart <= day and t4monthstart == month and t4yearstart == year) or (day <= t4dayend and month == t4monthend and year == t4yearend):    # Term 4
    term = 4
    print("It is currently the 4th term")
elif (t5daystart <= day and t5monthstart == month and t5yearstart == year) or (day <= t5dayend and month == t5monthend and year == t5yearend):    # Term 5
    term = 5
    print("It is currently the 5th term")
elif (t6daystart <= day and t6monthstart == month and t6yearstart == year) or (day <= t6dayend and month == t6monthend and year == t6yearend):    # Term 6
    term = 6
    print("It is currently the 6th term")
#If not a term, compare to see which term break it is
elif (t1dayend < day and t1monthend == month and t1yearend == year) or (day < t2daystart and month == t2monthstart and year == t2yearstart):    # 1st half term
    notterm = 1
    print("College is on break")
elif (t2dayend < day and t2monthend == month and t2yearend == year) or (day < t3daystart and month == t3monthstart and year == t3yearstart):    # Christmas break
    notterm = 2
    print("College is on break")
elif (t3dayend < day and t3monthend == month and t3yearend == year) or (day < t4daystart and month == t4monthstart and year == t4yearstart):    # Second half term
    notterm = 3
    print("College is on break")
elif (t4dayend < day and t4monthend == month and t4yearend == year) or (day < t5daystart and month == t5monthstart and year == t5yearstart):    # Easter break
    notterm = 4
    print("College is on break")
elif (t5dayend < day and t5monthend == month and t5yearend == year) or (day < t6daystart and month == t6monthstart and year == t6yearstart):    # Third half term
    notterm = 5
    print("College is on break")
else:    # Summer (or other)
    print("Year has ended")

# If term is not 0, state how long till end of term [(Term end date - current date) in days]
if term > 0:
    if term == 1:     # Days till end of term 1
        print ("There are " + str((datetime.date(int(t1yearend), int(t1monthend), int(t1dayend)) - today).days) + " days until the end of term")
    elif term == 2:   # Days till end of term 2
        print ("There are " + str((datetime.date(int(t2yearend), int(t2monthend), int(t2dayend)) - today).days) + " days until the end of term")
    elif term == 3:   # Days till end of term 3
        print("There are " + str((datetime.date(int(t3yearend), int(t3monthend), int(t3dayend)) - today).days) + " days until the end of term")
    elif term == 4:   # Days till end of term 4
        print ("There are " + str((datetime.date(int(t4yearend), int(t4monthend), int(t4dayend)) - today).days) + " days until the end of term")
    elif term == 5:   # Days till end of term 5
        print ("There are " + str((datetime.date(int(t5yearend), int(t5monthend), int(t5dayend)) - today).days) + " days until the end of term")
    elif term == 6:   # Days till end of term 6
        print ("There are " + str((datetime.date(int(t6yearend), int(t6monthend), int(t6dayend)) - today).days) + " days until the end of term")
    else:   # Absurdly unlikely, but there is a non-zero chance it might occur
        print("Something's clearly gone wrong here, the term variable shouldn't go higher than 6")
# If notterm is not 0, state how long till next term (and what term it will be)
elif notterm > 0:
    if notterm == 1:      # Days till start of term 2
        print ("There are " + str((datetime.date(int(t2yearstart), int(t2monthstart), int(t2daystart)) - today).days) + " days until the start of term 2")
    elif notterm == 2:    # Days till start of term 3
        print ("There are " + str((datetime.date(int(t3yearstart), int(t3monthstart), int(t3daystart)) - today).days) + " days until the start of term 3")
    elif notterm == 3:    # Days till start of term 4
        print ("There are " + str((datetime.date(int(t4yearstart), int(t4monthstart), int(t4daystart)) - today).days) + " days until the start of term 4")
    elif notterm == 4:    # Days till start of term 5
        print ("There are " + str((datetime.date(int(t5yearstart), int(t5monthstart), int(t5daystart)) - today).days) + " days until the start of term 5")
    elif notterm == 5:    # Days till start of term 6
        print ("There are " + str((datetime.date(int(t6yearstart), int(t6monthstart), int(t6daystart)) - today).days) + " days until the start of term 6")
    else:   # Absurdly unlikely, but there is a non-zero chance it might occur
        print("Something's clearly gone wrong here, the notterm variable shouldn't go higher than 5")
else:   # Either something's wrong or anything else is summer break
    print("Have a nice summer")

# Countdown till end of academic year
if term != 0 or notterm != 0:   #Check that they are actually in academic year
    print ("There are " + str((datetime.date(int(t6yearend), int(t6monthend), int(t6dayend)) - today).days) + " days until the end of the academic year")
else:   # Either something's wrong or anything else is outsied of the academic year
    print("See you next year")

# Test print for ensuring I have the right worksheet cell, or other value:
thing = ""
print(thing)
# Test print showing current date, and term start/end dates being pulled from the excel file
#print("\n", "Current date", day, month, year, "\n", "Term 1", t1daystart, t1monthstart, t1yearstart, "\t", t1dayend, t1monthend, t1yearend, "\n", "Term 2", t2daystart, t2monthstart, t2yearstart, "\t", t2dayend, t2monthend, t2yearend, "\n", "Term 3", t3daystart, t3monthstart, t3yearstart, "\t", t3dayend, t3monthend, t3yearend, "\n", "Term 4", t4daystart, t4monthstart, t4yearstart, "\t", t4dayend, t4monthend, t4yearend, "\n", "Term 5", t5daystart, t5monthstart, t5yearstart, "\t", t5dayend, t5monthend, t5yearend, "\n", "Term 6", t6daystart, t6monthstart, t6yearstart, "\t", t6dayend, t6monthend, t6yearend)