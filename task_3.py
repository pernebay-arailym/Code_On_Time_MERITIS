# Step 1: Read and parse the data
entries = []
with open("task3_meritis.txt", "r") as file:
    for line in file:
        entry_data = line.strip().split(",")
        entry = (int(entry_data[1]), 1)  # (timestamp, entry)
        exit = (int(entry_data[2]), -1)  # (timestamp, exit)
        entries.append(entry)
        entries.append(exit)

# Step 2: Sort the entries based on timestamps
entries.sort()

# Step 3: Initialize variables
max_athletes = 0
current_athletes = 0

# Step 4: Iterate through each entry
for timestamp, action in entries:
    current_athletes += action
    max_athletes = max(max_athletes, current_athletes)

# Step 5: Print the result
print("Maximum number of athletes present in the dressing room at any given time:", max_athletes)
