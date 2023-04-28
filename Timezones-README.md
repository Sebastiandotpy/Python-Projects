# Timezones

## Working with timezones

In this exercise, we will focus on working across nations and boundaries when sending products (packages) or booking meetings with our friends and clients.

- Convert your birthdate in German local Time to the time in New Zealand (Auckland)
- Coordinate with your Team based in Ireland, San Francisco (USA), Berlin (Germany) and Johannesburg (South Africa). You will be having a meeting with another Team at 13:35 (Moscow Time). Print out the respective times your colleagues will be meeting

##

## Usage

`datetime`, `dateutil` should be used in the following way

```
from datetime import datetime
from datetuil import tz
from datetutil.relativedelta import *
```

##

## Tasks

###

### Task 1

- Use your birthday or a friend's

Hint: use `tz.gettz()` method to setup the timezone.

```
birthday = datetime(..., tzinfo=...)
...

birthday_in_newzealand = birthday.astimezone(...)
```

###

### Task 2

Your team is a multinational one meeting a regional leader based in Moscow, Russia, with the following regions:

- Dublin / Ireland
- San Francisco / USA
- Berlin / Germany
- Johannesburg / South Africa

Write a Python script that will print out the different times the teams will meet.

- Your result should look like this, if meeting day is is 8/07/2021 at 13:35 Moscow time:

```
Irish participants will meet at: 11:35:00+01:00
German participants will meet at: 2021-08-01 12:35:00+02:00
South African participants will meet at: 2021-08-01 12:35:00+02:00
American participants will meet at: 2021-08-01 03:35:00-07:00
```

###

### Task 3

Write a Python program to convert a UNIX timestamp like `1626430738` to a readable date

```
07/16/2021, 12:18:58
```


























Import the datetime module and the tz submodule from the dateutil package: from datetime import datetime and from dateutil import tz. These modules are used for date and time-related calculations and conversions.

Define the birthdate as a datetime object with timezone information using datetime() and tz.gettz() functions: birthday = datetime(1990, 1, 1, 0, 0, tzinfo=tz.gettz('Europe/Berlin')). This sets the birthdate to January 1st, 1990, 12:00am (midnight) in the time zone "Europe/Berlin".

Print the original birthdate: print("Birthday in Germany:", birthday). This line simply prints the original birthdate in the German timezone.

Set the timezone for Auckland, New Zealand: auckland_tz = tz.gettz('Pacific/Auckland'). This sets the timezone to "Pacific/Auckland".

Convert the birthdate to the Auckland timezone using astimezone(): birthday_in_newzealand = birthday.astimezone(auckland_tz). This line converts the birthdate from German timezone to the Auckland timezone.

Print the converted birthdate: print("Birthday in New Zealand:", birthday_in_newzealand). This line simply prints the converted birthdate in the Auckland timezone.

Set the meeting time in Moscow using datetime() and tz.gettz() functions: meeting_time = datetime(2023, 5, 1, 13, 35, tzinfo=moscow_tz). This sets the meeting time to May 1st, 2023, 1:35 PM in the Moscow timezone.

Set a list of team cities: team_cities = ['Dublin/Ireland', 'San Francisco/USA', 'Berlin/Germany', 'Johannesburg/South Africa']. This creates a list of cities where team members are located.

Set a list of timezones corresponding to each team city using tz.gettz() function: team_tz = [tz.gettz('Europe/Dublin'), tz.gettz('America/Los_Angeles'), tz.gettz('Europe/Berlin'), tz.gettz('Africa/Johannesburg')]. This creates a list of timezone objects corresponding to each city in the team_cities list.

Loop through each team city and convert the meeting time to the local time of that city using astimezone() function:

"python
for city, tz in zip(team_cities, team_tz):
    local_time = meeting_time.astimezone(tz)
    print(f"{city} participants will meet at:", local_time)
This loop iterates over the team_cities and team_tz lists simultaneously using the zip() function, then converts the meeting time to the local time of that city using the astimezone() method. Finally, it prints out the meeting time for each city."

Print the result for Task 2: print("Task 2 result: see above"). This line just prints out a message indicating that the Task 2 result is shown above.

Set a UNIX timestamp value: unix_timestamp = 1626430738. This sets the UNIX timestamp to 1626430738.

Convert the UNIX timestamp to a datetime object using datetime.fromtimestamp(): date = datetime.fromtimestamp(unix_timestamp). This converts the UNIX timestamp to a datetime