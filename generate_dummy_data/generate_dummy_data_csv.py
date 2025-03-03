from faker import Faker
import random
import csv
import os

# Initialize Faker
fake = Faker()

# Number of records
num_records = 100

# Generate dummy data
data = []
for _ in range(num_records):
    entry = {
        "id": _ + 1,
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "phone": fake.phone_number(),
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat(),
        "company": fake.company(),
        "salary": round(random.uniform(30000, 120000), 2),  # Random salary
        "is_active": random.choice([True, False])  # Random boolean
    }
    data.append(entry)

print(f"Current working directory: {os.getcwd()}")
csv_file = "../data/dummy_data.csv"
dir_name = os.path.dirname(csv_file)  # Get the directory part of the path

# Check if the directory exists, if not, create it
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

# **Write to CSV**
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
print(f"CSV file '{csv_file}' created successfully!")