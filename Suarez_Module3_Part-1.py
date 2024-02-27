# Prompt the customer for the charge cost
food_charge = float(input("Please enter the cost of the food: $"))

# Calculate the tip (18% of the food charge)
tip = food_charge * 0.18

# Calculate the sales tax (7% of the food charge)
sales_tax = food_charge * 0.07

# Calculate the total price (food charge+tip+sales tax)
total_price = food_charge + tip + sales_tax

# Display the amounts
print(f"Tip: ${tip:.2f}")
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total Price: ${total_price:.2f}")
