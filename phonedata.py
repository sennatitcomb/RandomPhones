import csv
import random

fake_integers = [random.randint(10**9, 10**10 - 1) for _ in range(3000)]

# Format the fake integers with dashes
formatted_integers = [f"{str(number)[:3]}-{str(number)[3:6]}-{str(number)[6:]}" for number in fake_integers]

# Specify the file name
csv_file = 'fake_integers.csv'

# Write the formatted fake integers to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Assuming you want one column in the CSV file
    writer.writerow(['Formatted Fake Integers'])  # Header
    
    for formatted_number in formatted_integers:
        writer.writerow([formatted_number])

print(f"Formatted fake integers saved to {csv_file}")
