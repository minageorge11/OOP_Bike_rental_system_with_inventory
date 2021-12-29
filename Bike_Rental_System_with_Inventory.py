import calendar

class bike_rental:
    def __init__(self, ):
        self.rental_month = 0
        self.period = ""
        self.number_of_bikes = 0
        self.number_of_days = 0
        self.number_of_weeks = 0
        self.rental_day = 0
        self.week_days = {
            "0": "Monday",
            "1": "Tuesday",
            "2": "Wednesday",
            "3": "Thursday",
            "4": "Friday",
            "5": "Saturday",
            "6": "Sunday"
        }


#prints a calendar of the rental month with weekdays to make it easier to the rentee to select the first day of rent    
    def print_calendar(self, rental_month):
        calndr = calendar.Calendar()
        cal1 = []
        month_calendar = calndr.itermonthdays4(2022, rental_month)

        for x in month_calendar:
            cal1.append(list(x))

        for i in range(len(cal1)):
            day_of_week = cal1[i][-1] 
            cal1[i][-1] = self.week_days[str(day_of_week)]

        for y in cal1:
            if y[1] == rental_month: print(y)

#Asks the user to enter the month of the rent and validates the number
    def get_month(self):
        while True:
            self.rental_month = int(input("Please enter the Month # you want to rent in: "))
            if self.rental_month < 1 or self.rental_month > 12:
                print(" This is invalid month.")
                continue
            else: return(self.rental_month)

#Asks the user if they want to rent on daily or weekly basis, and validates the input.
    def get_period(self):
        while True:
            self.period = input("Enter \"Daily\" for daily rental, or enter \"Weekly\" for weekly rental: ")
            if self.period.lower() != "daily" and self.period.lower() != "weekly":
                print(" This is invalid period.")
                continue
            else: return(self.period)

#Asks the user to enter the number of bikes they want to rent and validates the number
    def get_number_of_bikes(self):
        while True:
            self.number_of_bikes = int(input("Enter number of bikes you want to rent: "))
            if self.number_of_bikes < 1:
                print(" This is invalid number of bikes.")
                continue
            else: return(self.number_of_bikes)

#If the user selected daily rental, asks the user to enter the number of days they want to rent and validates the number
    def get_number_of_rental_days_for_daily_rental(self):    
        while True: 
            self.number_of_days = int(input("Enter number of days you want to rent: "))
            if self.number_of_days >= 1: return(self.number_of_days)
            else:
                print("Thats invalid entry. Enter the number of days again: ")
                continue

#If the user selected Weekly rental, asks the user to enter the number of weeks they want to rent and validates the number
    def get_number_of_rental_weeks_for_weekly_rental(self):
        while True:
            self.number_of_weeks = int(input("Enter number of weeks you want to rent: "))
            if self.number_of_weeks >= 1: return(self.number_of_weeks)
            else:
                print("Thats invalid entry. Enter the number of weeks again: ")
                continue

#Asks the user to enter the first day of the rent and validates the number
    def start_day_of_rental(self):
        while True:
            self.rental_day = int(input("Enter the first day of the rent : "))
            if self.rental_day < 1 or self.rental_day > 31:
                print("This is invalid day.")
                continue
            else:
                return(self.rental_day)

#Checks the inventory have availble bikes in all the rent days
    def chech_availability(self):
        is_available = True
        first_day_of_rent = self.rental_day
        for i in range(self.number_of_days):
            if self.number_of_bikes > inventory[str([2022, self.rental_month, first_day_of_rent])]:
                is_available = False
                break
            else: first_day_of_rent += 1
        return is_available

#Update the inventory after the rental is confirmed by subtracting the number of rented bikes from the available inventory. Then prints the updated inventory.
    def update_inventory(self):
        print("Updated Inventory on rental days: ")
        first_day_of_rent = self.rental_day
        for p in range(self.number_of_days):
            inventory[str([2022, self.rental_month, first_day_of_rent])] -= self.number_of_bikes
            for key, value in inventory.items():
                if key == str([2022, self.rental_month, first_day_of_rent]):
                    print('Day: ', key, ' : ', 'Available # of bikes: ', value)
            first_day_of_rent += 1

#Update the inventory after returning the bikes by adding back the rented bikes to the available inventory.Then prints the updated inventory.

    def return_bike(self):
        print("Updated Inventory after returning the bikes: ")
        first_day_of_rent = self.rental_day
        for i in range(self.number_of_days):
            inventory[str([2022, self.rental_month, first_day_of_rent])] += self.number_of_bikes
            for key, value in inventory.items():
                if key == str([2022, self.rental_month, first_day_of_rent]):
                    print('Day: ', key, ' : ', 'Available # of bikes: ', value)
            first_day_of_rent += 1

    def print_inventory(self):
        first_day_of_rent = self.rental_day
        for i in range(self.number_of_days):
            for key, value in inventory.items():
                if key == str([2022, self.rental_month, first_day_of_rent]):
                    print('Day: ', key, ' : ', 'Available # of bikes: ', value)
            first_day_of_rent += 1


#Rent bikes function
    def rent_bike(self):
        while True:
            self.rental_month = self.get_month()   #1 ask the user to enter the month of the rent
            self.print_calendar(self.rental_month)  #2  prints a calendar of the rental month with weekdays to make it easier to the rentee to select the first day of rent  
            self.rental_day = self.start_day_of_rental()  #3  asks the user to enter the first day of the rent
            self.period = self.get_period()   #4 asks the user if they want to rent on daily or weekly basis
            self.number_of_bikes = self.get_number_of_bikes()   #5  asks the user for the number of bikes
            if self.period.lower() == "daily": #6 >> if the use chosed daily, ask the user to enter number of days
                self.number_of_days = self.get_number_of_rental_days_for_daily_rental()
                print("The rent will be in Month: {}, Day: {}, on {} basis, for {} day(s) and renting {} bike(s). \n".format(self.rental_month, self.rental_day, self.period.upper(), self.number_of_days, self.number_of_bikes ))
            elif self.period.lower() == "weekly": #>>If the use chosed weekly, ask the user to enter number of weekly
                self.number_of_weeks = self.get_number_of_rental_weeks_for_weekly_rental()
                print("The rent will be in Month: {}, Day: {}, on {} basis, for {} week(s) and renting {} bike(s). \n".format(self.rental_month, self.rental_day, self.period.upper(), self.number_of_weeks, self.number_of_bikes ))
            if self.period.lower() == "weekly": self.number_of_days = self.number_of_weeks * 7 #7 if the use chosed weekly, get the number of days by multiplying the number of weeks by 7
            self.check_available = self.chech_availability()  #8 check inventory availability of the requested number of bikes on selected days
            if not self.check_available: #9 if there isn't enough bikes available, repeat the process
                print("Sorry, We don't have that number of bikes in inventory. Please chose different days. Available inventory on the date you chosed is:")
                self.print_inventory()
                continue
            else: 
                self.update_inventory() #10 if there is available inventory, process the rent and update the inventory.
                break

#First, build an inventory of 20 bike available to rent for the entire year 2022, the inventory will be updated later based on the rent/return
inventory = {}
def build_inventory():
    calndr = calendar.Calendar()
    cal = []
    for k in range(1, 13):
        month_calendar = calndr.itermonthdays3(2022, k)
        for x in month_calendar:
            cal.append(list(x))
    for j in range(len(cal)):
        inventory[str(cal[j])] = 20
    return inventory
inventory = build_inventory()

user = bike_rental()
user2 = bike_rental()


user.rent_bike()
user2.rent_bike()

user.return_bike()
user2.return_bike()
