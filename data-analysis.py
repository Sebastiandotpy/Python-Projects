# Task 1: Count total number of users and print every 5th user
data = '''
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
25,Lissi,Davidovitz,ldavidovitzo@guardian.com,48.7.220.5'''

lines = data.split('\n')

# Count total number of users and print
num_users = len(lines)
print(f"Total number of users: {num_users}")

# Print every 5th user
print("Every 5th user:")
for i in range(4, num_users, 5):
    print(lines[i])

# Task 2: Print email address of each user
print("\nEmail address of each user:")
for line in lines[1:]:
    try:
        user_id, first_name, last_name, email, ip_address = line.split(',')
        print(f"User {user_id} email address: {email}")
    except IndexError:
        # Handle invalid data
        print(f"Invalid data: {line}")

# Task 3: Count number of users with email domain '.co.uk' and first or last name starting with 'K'
co_uk_count = 0
k_count = 0
for line in lines[1:]:
    try:
        # Check for email domain '.co.uk'
        if ".co.uk" in line.split(',')[3]:
            co_uk_count += 1

        # Check for first or last name starting with 'K'
        user_id, first_name, last_name, email, ip_address = line.split(',')
        if first_name.startswith('K') or last_name.startswith('K'):
            k_count += 1
    except (IndexError, ValueError):
        # Handle invalid data
        print(f"Invalid data: {line}")

# Print counts
print(f"\nNumber of users with email domain '.co.uk': {co_uk_count}")
print(f"Number of users with first or last name starting with 'K': {k_count}")

# Task 4: Print first name, first letter of last name, and masked IP address of each user
print("\nFirst name, first letter of last name, and masked IP address of each user:")
for line in lines[1:]:
    try:
        user_id, first_name, last_name, email, ip_address = line.split(',')
        masked_ip = ip_address[:7] + ".xxx.xxx"
        print(f"{first_name} {last_name[0]} {masked_ip}")
    except (IndexError, ValueError):
        # Handle invalid data
        print(f"Invalid data: {line}")

# Bonus task: Count number of users for each email domain and print top 3 domains
from collections import Counter
email_dict = Counter([line.split(',')[3].split('@')[1] for line in lines[1:]])
top_3_domains = email_dict.most_common(3)
print("\nTop 3 email domains:")
for domain, count in top_3_domains:
    print(f"{domain}: {count}")

       

       
