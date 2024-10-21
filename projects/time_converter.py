
# 1. Get number of seconds from the user.
# 2. Get number of hours.
# 3. Get the number of remaining minutes 
# 4. Get number of remaining seconds 
# 5. Display the result


total_second = float(input('Enter a number of seconds: '))
hours = total_second // 3600
minutes = (total_second // 60) % 60
seconds = total_second % 60

print('Here is the time in hours, minutes, and seconds:')
print('Hours:', hours)
print('Minutes:', minutes)
print('Seconds:', seconds)