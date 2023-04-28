from datetime import datetime, timedelta

# Task 1 Subtract 15 days from the current date
current_datetime = datetime.now()
print("Task 1:")
print("Current datetime:", current_datetime)

# timedelta to subtract 15 days from current date
delta = timedelta(days=15)
new_datetime = current_datetime - delta

# Format datetime as string
formatted_datetime = new_datetime.strftime('%Y-%m-%d')
print("15 days ago:",  formatted_datetime)

print("Task 1 result:", formatted_datetime)

print("\n--------------------------------------------\n")

# Task 2 Add 7 days to the current date
print("Task 2 Add 7 days to the current date")
print("Current datetime:", current_datetime)

# timedelta to add 7 days to current date
delta = timedelta(days=7)
new_datetime = current_datetime + delta

# Format datetime as string
formatted_datetime = new_datetime.strftime('%Y-%m-%d')
print("7 days from now:", formatted_datetime)

print("Task 2 result:", formatted_datetime)

print("\n--------------------------------------------\n")

# Task 3 Write a reminder message for a customer
print("Task3 Write a reminder message for a customer")

# Set the current date to  january 1st, 2020
current_date = datetime(year=2020, month=1, day=1)
print("Current date:", current_date.strftime('%Y-%m-%d'))


# Calulate the due date by adding 25 days
due_date = current_date + timedelta(days=25)
print("Due date:", due_date.strftime('%Y-%m-%d'))


# Contruct and print the reminder message
customer_name = "Friedrich"
rent_amount= 300
message = f"Hello {customer_name}, your rent of {rent_amount} $ is due on {due_date.strftime('%d %B, %Y')}."
print(message)

print("Task 3 result:", message)