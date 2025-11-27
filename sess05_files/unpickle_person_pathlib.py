# Python script to unpickle the person's details from the 'person_pathlib.txt' file
# and display them

# Import the required modules
import pickle
from pathlib import Path
from person import Person 
import os

# Variables to hold the path to the 'person_os.txt'
file_path = os.path.abspath(os.path.join(os.getcwd(), "..", "files/person_pathlib.txt"))

try:
    # Open the file 
    # Use pickle.load() to unpickle the object from the file
    with open(file_path, "rb") as f:
        unpickled_person = pickle.load(f)

    # Display the unpickled object's details
    print("\n--- Unpickled Person Details ---")
    print(f"Name: {unpickled_person.name}")
    print(f"Age: {unpickled_person.age}")
    print("--------------------------------")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please ensure the pickling script was run first.")
