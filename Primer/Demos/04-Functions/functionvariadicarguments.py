def display_favourite_things(name, *things, place):
  print(f"Favourite things for {name} who lives in {place}")
  for thing in things:
    print("  %s" % thing)

# Usage (i.e. client code)
display_favourite_things("Kevin", "Jayne", "Emily", "Thomas", 3, "Swans", place="Bristol")

# ("Jayne", "Emily", "Thomas", 3, "Swans")