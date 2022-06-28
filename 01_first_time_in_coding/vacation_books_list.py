from math import floor
pages = int(input())
pages_hour = int(input())
days = int(input())

time_in_hours = pages / pages_hour
time_in_days = time_in_hours / days
print(floor(time_in_days))