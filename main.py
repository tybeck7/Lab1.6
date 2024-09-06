#Tyler Beck
#CISP 300
#September 4, 2024

# This program will calculate how many calories are burned based on the number of steps taken throughout a day.
# This is based on 2000 steps equals 1 mile, and 1 mile of walking burns 65 calories.

# Ask for user input
weekDay = input("Enter the day of the week: ")
stepsTaken = int(input("Enter the number of steps reported on the pedometer: "))

# The calculations
milesWalked = float(stepsTaken) / 2000  # Treating milesWalked as a Real (float)
caloriesLost = milesWalked * 65  # Treating caloriesLost as a Real (float)

# Display the output
print("The following is data for", weekDay + ":")
print("Walking", format(milesWalked, ".2f"), "miles results in", format(caloriesLost, ".2f"), "calories lost.")
