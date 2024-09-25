from datetime import datetime, timedelta

def generate_dates(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date.strftime('%d%m%Y')
        current_date += timedelta(days=1)

# Define start and end dates
y = int(input('Enter the starting day in DD format: '))
p = int(input('Enter the starting month in MM format: '))
a = int(input('Enter the starting year in YYYY format: '))
z = int(input('Enter the ending date in DD format: '))
q = int(input('Enter the ending month in MM format: '))
b = int(input('Enter the ending year in YYYY format: '))
start_date = datetime(a, p, y)  # Example start date
end_date = datetime(b, q, z)  # Example end date
count = 0
# Generate dates and write to a file
with open('birthdates_wordlist.txt', 'w') as file:
    for date in generate_dates(start_date, end_date):
        file.write(date + '\n')
        count = count + 1
print(f'The wordlist file has been created with the file name "birthdates_wordlist.txt" containing {count} number of words')
#adding customDOB1