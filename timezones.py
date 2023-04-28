from datetime import datetime
from dateutil import tz

# Task 1 Convert your birthdate in German local Time to the time in New Zealand
print("Task 1:")
# Set birthday to datetime object
birthday = datetime(1990, 1, 1, 0, 0, tzinfo=tz.gettz('Europe/Berlin'))
print("Birthday in Germany:", birthday)

# Set timezone to Auckland
auckland_tz = tz.gettz('Pacific/Auckland')
# Convert birthday to Auckland time
birthday_in_newzealand = birthday.astimezone(auckland_tz)
print("Birthday in New Zealand:", birthday_in_newzealand)
print("Task 1 result:", birthday_in_newzealand)
print("\n-----------------------------------------------------------------\n")

# Task 2 Coordinate with your Team based in Ireland, San Francisco (USA), Berlin (Germany) and Johannesburg (South Africa).
print("Task 2:")
# Set meeting time to Moscow time
moscow_tz = tz.gettz('Europe/Moscow')
meeting_time = datetime(2021, 8, 7, 13, 35, tzinfo=moscow_tz)
print("Meeting time (Moscow time):", meeting_time)

# Set list of team cities
team_cities = ['Irish', 'German', 'South African', 'American']

# Set timezone for each team city
team_tz = [tz.gettz('Europe/Dublin'), tz.gettz('Europe/Berlin'),
           tz.gettz('Africa/Johannesburg'), tz.gettz('America/Los_Angeles')]

# Convert meeting time to each team's local time and print
for city, tz in zip(team_cities, team_tz):
    local_time = meeting_time.astimezone(tz)
    print(f"{city} participants will meet at: {local_time:%Y-%m-%d %H:%M:%S%z}")

print("Task 2 result: see above")
print("\n-----------------------------------------------------------------\n")

# Task 3 Write a Python program to convert a UNIX timestamp like 1626430738 to a readable date
print("Task 3:")
# Set UNIX Timestamp
unix_timestamp = 1626430738
print("UNIX timestamp:", unix_timestamp)

# Convert UNIX timestamp to a datetime object
date = datetime.fromtimestamp(unix_timestamp)

# Format datetime object as string
formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")
print("Readable date:", formatted_date)

print("Task 3 result:", formatted_date)
