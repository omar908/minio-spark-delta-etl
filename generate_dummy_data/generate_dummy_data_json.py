from faker import Faker
import os
import random
import json

# Initialize Faker
fake = Faker()

# Configuration
total_records = 100  # Total number of records
output_folder = "../data/json_batches"  # Folder for JSON files

# Ensure output directory exists
print(f"Current working directory: {os.getcwd()}")
os.makedirs(output_folder, exist_ok=True)

# Generate and save data in batches
data = []
for i in range(total_records):
    entry = {
        "id": i + 1,
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address().replace("\n", ", "),  # Replace newline with comma and space
        "phone": fake.phone_number(),
        "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat(),
        "company": fake.company(),
        "salary": round(random.uniform(30000, 120000), 2),
        "is_active": random.choice([True, False])
    }
    data.append(entry)

for entry in data:
    file_name = os.path.join(output_folder, f"record_{entry['id']:04}.json")
    with open(file_name, "w") as file:
        json.dump(entry, file, indent=4)
    print(f"Created: {file_name}")

print(f"JSON files created successfully in '{output_folder}'!")
print("JSON batch generation complete!")