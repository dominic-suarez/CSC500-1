# Ask the customer for the number of books purchased
num_books = int(input("Please enter the number of books you have purchased this month: "))

# Determine the number of points based on the number of books purchased
if num_books == 0:
    points = 0
elif num_books == 1:
    points = 0
elif num_books == 2:
    points = 5
elif num_books == 3:
    points = 5
elif num_books == 4:
    points = 15
elif num_books == 5:
    points = 15
elif num_books == 6:
    points = 30
elif num_books == 7:
    points = 30
elif num_books >= 8:
    points = 60
    
# Display the number of points earned
if points >= 0:
    print(f"You have earned {points} points this month!")
