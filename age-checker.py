from datetime import datetime, timedelta
import pytz

def get_user_age(date_of_birth):
    # convert date string to datetime object
    dob = datetime.strptime(date_of_birth, '%d-%m-%Y')
    # calculate number of days since birth
    num_of_days = datetime.now() - dob
    # calculate age in years
    age = int(num_of_days.days / 365.2425)
    return age

def age_checker(age_of_user):
    if age_of_user < 18:
        print("\nYou need to be 18 years and above to create an account.\n")
        return False
    elif age_of_user > 150:
        print("\nYou need to be 150 years or younger to create an account.\n")
        return False
    else:
        print(f"\nYou are {age_of_user} years old, you can create an account.\n")
        return True

def get_user_info():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    print(f"\nYour name is {first_name} {last_name}, your username is {username}, and your email is {email}.\n")

def send_newsletters(customer_emails):
    for email in customer_emails:
        user_name = email.split('@')[0]
        print(f"Email sent to user with username {user_name} with email {email}")

def run_task(current_date, send_date, customer_emails):
    if current_date == send_date:
        send_newsletters(customer_emails)
        send_date += timedelta(days=5)
        print(f"Next newsletter send date: {send_date}")
    else:
        print(f"Newsletters will be sent later. Next send date is {send_date}")
    return send_date

customer_emails = ['testl@test.com', 'test2@test.com', 'test3@test.com', 'test4@test.com', 'test5@test.com', 'test6@test.com', 'test7@test.com', 'test8@test.com', 'test9@test.com', 'test10@test.com', 'test11@test.com', 'test12@test.com', 'test13@test.com', 'test14@test.com', 'test15@test.com', 'test16@test.com', 'test17@test.com', 'test18@test.com', 'test19@test.com', 'test20@test.com']

attempts = 5

while attempts > 0:
    date_of_birth = input("Enter your date of birth in the format DD-MM-YYYY: ")
    age = get_user_age(date_of_birth)
    if age_checker(age):
        get_user_info()
        # set timezone to CET
        timezone = pytz.timezone('CET')
        # set send date to next 5th day at 10:00 AM
        send_date = datetime.now(tz=timezone) + timedelta(days=(5 - datetime.now(tz=timezone).weekday()) % 5) + timedelta(hours=10)
        print(f"\nNewsletter service will start sending newsletters every 5 days, starting from {send_date}\n")
        break
    else:
        attempts -= 1
        if attempts == 0:
            print("Maximum number of attempts reached. Please contact support.")
            break

current_date = datetime.now(tz=timezone)

while True:
    current_date = datetime.now(tz=timezone)
    send_date = run_task(current_date, send_date, customer_emails)
    # wait for 1 hour before checking
