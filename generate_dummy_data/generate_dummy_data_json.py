from faker import Faker
import os
import random
import json

# Initialize Faker
fake = Faker()

# Configuration
total_records = 100  # Total number of records
batch_size = 10      # Entries per file
output_folder = "../data/json_batches"  # Folder for JSON files

# Ensure output directory exists
print(f"Current working directory: {os.getcwd()}")
os.makedirs(output_folder, exist_ok=True)

# Generate and save data in batches
for batch_num in range(total_records // batch_size):
    data = []
    for _ in range(batch_size):
        entry = {
            "id": batch_num * batch_size + _ + 1,
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

    # Create a unique filename for each batch
    padded_batch_num = f"{batch_num+1:04}"
    file_name = f"{output_folder}/batch_{padded_batch_num}.json"

    # Write the batch to a JSON file
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Created: {file_name}")

print("JSON batch generation complete!")