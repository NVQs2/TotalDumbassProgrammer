# Michael Carnall - Started 5/12/2019

# Let's try and make Counter till the end of term

# Ideas (Let's make it unnecessarily complicated)
# Store term dates in file, say spreadsheet, and pull from there? (allowing for easy changing each year by staff) - Done (NOW RETURNING MONTHS AS A NUMERICAL VALUE! HOORAY!)
# When not a term, state when the next term starts?
# State how many days before end of last term?

# For getting current date:
import datetime
current = datetime.datetime.now(datetime.timezone.utc)
year = 2019
#current.year
month = 9
#current.month
day = 2
#current.day
hour = current.hour
minute = current.minute
second = current.second
# import stuff for reading the spreadsheet:
import xlrd
workbook = xlrd.open_workbook(r'Term Dates.xlsx')
worksheet = workbook.sheet_by_name('Term Dates')

# Find way to convert month to number from 1-12 - list.index() function:
monthlist = ["Don't want index() returning 0 so here's a placeholder", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Variable from denoting if term or break (and which) - I have a hunch I'll need these later:
term = 0
notterm = 0

# Current year's terms (pulled from excel file):
# Term 1:
t1daystart = worksheet.cell(2, 1).value
t1monthstart = monthlist.index(worksheet.cell(2,2).value)
t1year = worksheet.cell(2, 3).value
t1dayend = worksheet.cell(2, 4).value
t1monthend = monthlist.index(worksheet.cell(2,5).value)
# Term 2:
t2daystart = worksheet.cell(3, 1).value
t2monthstart = monthlist.index(worksheet.cell(3,2).value)
t2year = worksheet.cell(3, 3).value
t2dayend = worksheet.cell(3, 4).value
t2monthend = monthlist.index(worksheet.cell(3,2).value)
# Term 3:
t3daystart = worksheet.cell(4, 1).value
t3monthstart = monthlist.index(worksheet.cell(4,2).value)
t3year = worksheet.cell(4, 3).value
t3dayend = worksheet.cell(4, 4).value
t3monthend = monthlist.index(worksheet.cell(4,2).value)
# Term 4:
t4daystart = worksheet.cell(5, 1).value
t4monthstart = monthlist.index(worksheet.cell(5,2).value)
t4year = worksheet.cell(5, 3).value
t4dayend = worksheet.cell(5, 4).value
t4monthend = monthlist.index(worksheet.cell(5,2).value)
# Term 5:
t5daystart = worksheet.cell(6, 1).value
t5monthstart = monthlist.index(worksheet.cell(6,2).value)
t5year = worksheet.cell(6, 3).value
t5dayend = worksheet.cell(6, 4).value
t5monthend = monthlist.index(worksheet.cell(6,2).value)
# Term 6:
t6daystart = worksheet.cell(7, 1).value
t6monthstart = monthlist.index(worksheet.cell(7,2).value)
t6year = worksheet.cell(7, 3).value
t6dayend = worksheet.cell(7, 4).value
t6monthend = monthlist.index(worksheet.cell(7,2).value)

# Stating who made it and when
print("Written by Michael Carnall: 5/12/2019 - " + str(day) + "/" + str(month) + "/" + str(year) + "\n")

# State current time and date:
print("The time is " + str(hour) + ":" + str(minute) + ":" + str(second) +
      " UTC on " + str(day) + "-" + str(month) + "-" + str(year))

# Compare if current day, month and year are within first term start and end dates:
if t1daystart <= day <= t1dayend and t1monthstart <= month <= t1monthend and t1year == year:
    term = 1
    print("It is currently the 1st term")
elif t1dayend < day < t2daystart and t1monthend < month < t2monthstart and t1year == year:
    notterm = 1
    print("College is on break")
else:
    print("nope")

# Test print for ensuring I have the right worksheet cell, or other value:
thing = ""
print(thing)