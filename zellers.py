class DateCalculator:
    def __init__(self,year : int, month:int, day:int):
        if 3<=month<=14:
            self.month = month
            self.year=year
            self.day=day
        else:
            print('Enter a valid month, from 3 to 14')
            return 
        
    def calculate(self):
        K = self.year % 100
        J = self.year // 100
        h = (self.day + (13*(self.month + 1)//5) + K + (K//4) + (J//4) + 5 * J) % 7

        return h


weekdays = list(('Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'))

        
month = int(input('Enter the month(Jan = 13, Feb = 14, Mar = 3) : '))
day = int(input('Enter the day : '))
year = int(input('Enter the year : '))

date = DateCalculator(year=year, month=month, day=day)

print(weekdays[date.calculate()])