import os
import subprocess

# Define the directories as a list
directories = [
    "/home/localusr/docker/plex/media/Movies",
    "/home/localusr/docker/plex/media/Shows"
]

# Function to check if the directories are empty
def is_directory_empty(directory):
    # os.listdir lists the content in the specified directory
    return len(os.listdir(directory)) == 0

# Loops over the directories list and check if the directories are empty
for directory in directories:
    if is_directory_empty(directory):
        print(f"{directory} is empty.")
    else:
        print(f"{directory} is not empty.")
