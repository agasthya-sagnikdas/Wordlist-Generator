from datetime import datetime, timedelta

def generate_dates(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date.strftime('%d%m%Y')
        current_date += timedelta(days=1)

# Define start and end dates
start_date = datetime(2000, 1, 1)  # Example start date
end_date = datetime(2000, 1, 31)  # Example end date

# Generate dates and write to a file
with open('birthdates_wordlist.txt', 'w') as file:
    for date in generate_dates(start_date, end_date):
        file.write(date + '\n')
#adding customDOB1