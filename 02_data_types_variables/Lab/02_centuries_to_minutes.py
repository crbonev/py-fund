century = int(input())
year = century * 100
dayz = year * 365.2422
days = int(dayz)
hours = days * 24
minutes = hours * 60
print(f'{century} centuries = {year} years = {days} days = {hours} hours = {minutes} minutes')