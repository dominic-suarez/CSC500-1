# Ask the number of years

num_years = int(input("Please enter the number of years: "))

# Initialize total rainfall and month counter

total_rainfall = 0

month_counter = 0

# Outer loop for each year

for year in range(num_years):

    print(f"\nYear {year+1} Rainfall:")

     # Inner loop for each month

    for month in range(1, 13):

        # Ask for inches of rainfall for that month

        rainfall = float(input(f"Enter the rainfall for month {month}: "))

        # Add the rainfall to the total

        total_rainfall += rainfall

        # Increment the month counter

        month_counter += 1

# Calculate the average rainfall

avg_rainfall = total_rainfall / month_counter

# Display total months, total inches of rainfall and average rainfall per month.

print(f"\nTotal months: {month_counter}")

print(f"Total inches of rainfall: {total_rainfall:.2f} inches")

print(f"Average rainfall per month: {avg_rainfall:.2f} inches")
