# Write your code below:
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

#Positional Arguments
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")

#Keyword Arguments
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")

#Default Arguments
trip_planner("Brooklyn", "Queens")