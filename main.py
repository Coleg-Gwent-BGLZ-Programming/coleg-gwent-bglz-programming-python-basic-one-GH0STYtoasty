# Get basic details
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Work out birth year and store with current year in a tuple
current_year = 2025
birth_year = current_year - age
year_info = (birth_year, current_year)

# Collect hobbies (using a set so they are unique)
hobbies = set()
print("Enter hobbies (type 'done' to finish):")
while True:
    hobby = input("Hobby: ")
    if hobby.lower() == "done":
        break
    hobbies.add(hobby)

# Store everything in a dictionary
user_data = {
    "Name": name,
    "Age": age,
    "Hobbies": list(hobbies),
    "Year Info": year_info
}

# Display the information back to the user
print(f"\nHello {user_data['Name']}, age {user_data['Age']}.")
print(f"Born in {user_data['Year Info'][0]}, current year {user_data['Year Info'][1]}.")
print("Hobbies:", ", ".join(user_data["Hobbies"]))
