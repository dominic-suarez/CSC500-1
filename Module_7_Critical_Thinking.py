# Initialize key value pairs.
course_rooms = {
    "CS101": "3004",
    "CS102": "4501",
    "CS103": "6755",
    "NT110": "1244",
    "CM241": "1411"
}

course_instructors = {
    "CS101": "Haynes",
    "CS102": "Alvarado",
    "CS103": "Rich",
    "NT110": "Burke",
    "CM241": "Lee"
}

course_times = {
    "CS101": "8:00 am",
    "CS102": "9:00 am",
    "CS103": "10:00 am",
    "NT110": "11:00 am",
    "CM241": "1:00 pm"
}

# Ask the user for input until they decide to exit
while True:
    course_number = input("Please enter a course number (or type 'q' to quit): ").upper()

    if course_number == "Q":
        break

    if course_number in course_rooms:
        print(f"Room Number: {course_rooms[course_number]}")
        print(f"Instructor: {course_instructors[course_number]}")
        print(f"Meeting Time: {course_times[course_number]}")
        print()
    else:
        print("Invalid course number. Please try again.")
        print()
