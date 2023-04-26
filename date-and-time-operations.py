# Task 1: Import the datetime module.
import calendar
import datetime

# Use the datetime.now() method to create a datetime object and store it in a variable called current_datetime.
current_datetime = datetime.datetime.now()

#  Use the year attribute of the current_datetime object to print out the current year.
print("Current year:", current_datetime.year)

# Task 2
# Create a datetime object for the provided date (2021, 7, 14) and store it in a variable called some_date.
some_date = datetime.datetime(2021, 7, 14)

# Use the weekday() method of the some_date object to print out the weekday of the week as a number between 0 and 6.
print("Weekday of the week:", some_date.weekday())

# Task 3
# Import the calendar module.

# Use the isleap() method of the calendar module to determine whether the year  2021 is a leap year.
if calendar.isleap(2021):
    print("2021 is a leap year")
else:
    print("2021 is not a leap year")

# Task 4
# Ask the user to input a date string in the format of "YYYY-MM-DD"
while True:
    date_string = input("Enter a date in the format of 'YYYY-MM-DD': ")
    try:
        # Use the strptime() method of the datetime module to convert the user-provided string into a datetime object.
        # You'll need to provide the format of the string as the second argument to strptime().
        date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        break
    except ValueError:
        # Catch any value errors that occur if the user inputs an invalid date format
        print("Invalid date format. Please enter the date in the format of 'YYYY-MM-DD'.")

# Print out the variable to verify that the conversion was successful.
print("Datetime object:", date_object)

# Check if the year of the date is a leap year using the calendar module
if calendar.isleap(date_object.year):
    print(f"The year {date_object.year} is a leap year")
else:
    print(f"The year {date_object.year} is not a leap year")
