Nothing like a chunk of fake data! We are getting semi-realistic over here.
​
Here, you are given a list of fake user data. Start by copying the following code into your own Python file. After that you will be given tasks to do with the data.
​
```py
data = """id,first_name,last_name,email,ip_address
1,Jennine,Kohnert,jkohnert0@disqus.com,45.55.73.106
2,Katalin,Nolda,knolda1@123-reg.co.uk,223.30.112.215
3,Atalanta,Kaming,akaming2@gmpg.org,254.219.7.208
4,Kassie,Covell,kcovell3@cafepress.com,150.145.187.71
5,Vonni,Dignam,vdignam4@cafepress.com,138.219.98.53
6,Billie,Neubigging,bneubigging5@addthis.org,180.79.192.175
7,Etan,Peers,epeers6@cafepress.com,199.1.3.70
8,Pail,Walcher,pwalcher7@cafepress.com,199.170.155.126
9,Edlin,Kosel,ekosel8@columbia.edu,217.59.107.252
10,Jennifer,Tibalt,jtibalt9@sun.com,73.29.190.227
11,Douglas,Howe,dhowea@cafepress.com,93.94.19.71
12,Galina,Antoniewski,gantoniewskib@freewebs.com,69.177.160.104
13,Emelita,Pauer,epauerc@house.gov,178.243.169.131
14,Edmon,Cleugh,POTATOKING.2000@furl.net,100.219.252.98
15,kyo,zipulimakkarakeitto,kz@guardian.com,78.226.120.240
16,Harlin,Goodrich,hgoodrichf@guardian.com,232.242.92.122
17,Paddie,Brittain,pbrittaing@jigsy.com,230.116.80.29
18,Blisse,Barbrook,bbarbrookh@nytimes.com,153.237.126.205
19,Latia,Roughey,lrougheyi@guardian.co.uk,184.128.166.8
20,Gregoire,Castelow,gcastelowj@51.la,87.181.120.134
21,lorenza,kurn,ljurnk@nsw.gov.au,192.238.146.135
22,Dulciana,Wilce,dwilcel@noaa.gov,234.245.232.7
23,Boyd,Sponton,bspontonm@guardian.com,106.75.217.74
24,Lenora,Issard,lissardn@guardian.com,167.91.15.190
25,Lissi,Davidovitz,ldavidovitzo@guardian.com,48.7.220.5"""
```
​
## TASKS
​
### Task 1
​
- Split the string into a list of strings
    - One line of data is one item in the list
    - Save the list of strings in a variable called `lines`
    - Print the amount of lines
​
- Loop over the lines using a `for` loop and print every 5th line
​
### Task 2
​
- Loop over the lines again
    - Skip the first line (called the header line)
    - Split each line by the commas, saving the result to a variable
    - Using that variable, print only the email addresses of each user
​
### Task 3
​
- Find out and print how many users have an email address with `.co.uk` in it
- Find out and print how many users first name OR last name starts with a "K" (uppercase or lowercase)
​
### Task 4
​
- For each user, print out a minified list including
​
    - Their first name
    - The first character of their last name
    - The first two octets of their IP address followed by `.xxx.xxx`
​
The output would look like this for the first three users:
​
        Jennine K., 45.55.xxx.xxx
        Katalin N., 223.30.xxx.xxx
        Atalanta K., 254.219.xxx.xxx
​
### OPTIONAL BONUS TASK
​
Statistics! Figure print out what are the top 3 most popular email address domains of all users. Print also the amount of users who have those e-mail address domains. The output might look like this (not the real data analyzed here):
​
        Statistics for top 3 email address domains of our users:
            hotmail.com - 51 users
            gmail.com   - 49 users
            yahoo.com   - 30 users
