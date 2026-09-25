years = int(input("Years of data: "))

total_rainfall = 0.0

for year in range(1, years + 1):
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall for year {year}, month {month}: "))
        total_rainfall += rainfall

total_months = years * 12
average_rainfall = total_rainfall / total_months

print("\n" + "="*30)
print(f"Total months: {total_months}")
print(f"Total rainfall: {total_rainfall:.2f}")
print(f"Average rainfall: {average_rainfall:.2f}")