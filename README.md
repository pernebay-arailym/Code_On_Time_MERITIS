

## Longest Progression Finder

### Overview

This Python script identifies the longest non-decreasing sequence of integers from a dataset stored in a text file (`data_task2_meritis.txt`). It reads the data, processes it to find the longest progression, and prints the sequence.

### Functionality

- **find_longest_progression(data):**
  - Iterates through the dataset to find the longest non-decreasing sequence (`progression`).
  - Updates `longest_progression` whenever a longer sequence is found.

- **read_data(file_path):**
  - Reads integers from the specified text file (`data_task2_meritis.txt`).
  - Returns a list of integers extracted from each line in the file.

- **Main Execution (`main` function):**
  - Calls `read_data` to retrieve the dataset from the file.
  - Calls `find_longest_progression` to determine the longest progression in the dataset.
  - Prints the longest progression found.

### Notes

- **Algorithm:** Implements a greedy algorithm to efficiently find the longest non-decreasing sequence in the dataset.
  
- **File Handling:** Assumes the dataset is stored in a text file (`data_task2_meritis.txt`) with each integer on a new line.

- **Performance:** The script handles datasets of varying sizes, determining the longest progression in an optimal manner.

- **Customization:** Modify `file_path` to point to a different dataset file for analysis. Adjust the code to find different types of progressions or sequences based on specific requirements.

