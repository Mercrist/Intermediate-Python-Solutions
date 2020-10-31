class Date:
    '''class to represent a date'''

    def __init__(self,month,day,year):
        '''Date(month,day,year) -> Date'''
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        '''str(Date) -> str
        returns date in readable format'''
        # list of strings for the months
        months = ['','Jan','Feb','Mar','Apr','May','Jun','Jul',
                  'Aug','Sep','Oct','Nov','Dec']
        output = months[self.month] + ' ' # month
        output += str(self.day) + ', '  # day
        output += str(self.year)
        return output

    def go_to_next_day(self):
        '''Date.go_to_next_day()
        advances the date to the next day'''
        # list with the days in the month
        daysInMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        # check for leap year
        isLeapYear = self.year%4 == 0 and \
                     (self.year%100 != 0 or self.year%400 == 0)
        if isLeapYear:
            daysInMonth[2] = 29  # Feb gets an extra day
        # advance the day
        self.day += 1
        # check if we need a new month
        if self.day > daysInMonth[self.month]:
            self.day = 1
            self.month += 1
        # check if we need a new year
        if self.month == 13:
            self.month = 1
            self.year += 1
# test cases
d1 = Date(6,11,2014)
print(d1)
d1.go_to_next_day()
print(d1)
# new month
d2 = Date(9,30,2005)
print(d2)
d2.go_to_next_day()
print(d2)
# leap year tests
d3 = Date(2,28,2011) # not a leap year
print(d3)
d3.go_to_next_day()
print(d3)
d4 = Date(2,28,2016) # is a leap year
print(d4)
d4.go_to_next_day()
print(d4)
# happy new year!
d5 = Date(12,31,2014)
print(d5)
d5.go_to_next_day()
print(d5)
