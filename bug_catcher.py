# The starting line of code sets it so the value is set to zero.
total_bugs = 0

 # This allows the days to be only set for five days instead of seven.
for day in range (1, 6):
    bugs = int(input(f"How many bugs were caught for day {day}: "))

    # This code makes it so that the bugs are added to the next day and replace the value of zero.
    total_bugs += bugs

# This shows how many bugs were accumulated over the five days.
print(f"Total bugs caught: {total_bugs}")