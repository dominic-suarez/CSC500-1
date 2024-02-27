# Prompt the user for the current time in military time
current_time = int(input("Please enter the current time at the current hour (0-23): "))

# Prompt the user for the number of hours to wait for the alarm
hours_to_wait = int(input("Please enter when you want the alarm to go off: "))

# Calculate the time when the alarm goes off (current_time + hours_to_wait) 
alarm_time = (current_time + hours_to_wait) % 24

# Display the time in 24-hour format
print(f"The alarm is set to go off in {alarm_time} hours.")

