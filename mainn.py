import csv
from faker import Faker
import random

# Initialize Faker instance
fake = Faker()

# Generate random student data
data = [["id", "student_id", "first_name", "last_name", "course_name", "mark"]]

for i in range(14, 500):
    student_id = f"N0{random.randint(100000, 999999)}M"
    first_name = fake.first_name()
    last_name = fake.last_name()
    course_name = "graphics"
    mark = random.randint(40, 100)
    data.append([i, student_id, first_name, last_name, course_name, mark])

# Write data to CSV file
filename = "student_data.csv"

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{filename}' has been generated with 3000 rows of random student data.")