honorific = input("Honorific, e.g. Mr. or Mrs.")
first_name = input("What's your first name? ")
last_name = input("What's your last name? ")

formatted_name = f"{honorific} {first_name[0].upper()}. {last_name.title()}"

print(formatted_name)