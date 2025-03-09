from faker import Faker
import random
import csv
import os
import json

fake = Faker()

def generate_dummy_data(num_records=100):
    # Generate a list of dummy data entries
    data = []
    for i in range(num_records):
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
    return data

def write_csv(data, csv_file="../data/dummy_data.csv"):
    # Write a list of dictionaries to a CSV file
    dir_name = os.path.dirname(csv_file)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"CSV file '{csv_file}' created successfully!")

def write_json(data, output_folder="../data/json_records"):
    # Write a list of dictionaries to individual JSON files.
    os.makedirs(output_folder, exist_ok=True)

    for entry in data:
        file_name = os.path.join(output_folder, f"record_{entry['id']:04}.json")
        with open(file_name, "w") as file:
            json.dump(entry, file, indent=4)
        print(f"Created: {file_name}")
    
    print(f"JSON files created successfully in '{output_folder}'!")


# def write_json_batches(total_records=100, batch_size=10, output_folder="../data/json_batches"):
#     # Generate dummy data in batches and write each batch to a JSON file
#     os.makedirs(output_folder, exist_ok=True)
#     num_batches = total_records // batch_size
#     for batch_num in range(num_batches):
#         data = []
#         for _ in range(batch_size):
#             entry = {
#                 "id": batch_num * batch_size + _ + 1,
#                 "name": fake.name(),
#                 "email": fake.email(),
#                 "address": fake.address().replace("\n", ", "),  # Replace newline with comma and space
#                 "phone": fake.phone_number(),
#                 "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat(),
#                 "company": fake.company(),
#                 "salary": round(random.uniform(30000, 120000), 2),
#                 "is_active": random.choice([True, False])
#             }
#             data.append(entry)
#         padded_batch_num = f"{batch_num+1:04}"
#         file_name = f"{output_folder}/batch_{padded_batch_num}.json"
#         with open(file_name, "w") as file:
#             json.dump(data, file, indent=4)
#         print(f"Created: {file_name}")
#     print("JSON batch generation complete!")

if __name__ == "__main__":
    # Generate both CSV and JSON files.
    write_csv(generate_dummy_data(100))
    write_json(generate_dummy_data(100))